<?php

namespace App\Extractors;

use App\Extractors\AbstractExtractor;
use Wikidata\Wikidata;

class WikidataExtractor extends AbstractExtractor
{
  protected string $mappingName = 'wikidata';

  protected function connection()
  {
    return;
  }

  protected function fetch()
  {
    $wikidata = new Wikidata();
    $wikidataObject = $wikidata->get($this->sourceId);

    return $wikidataObject;
  }

  protected function parse($rawData): array
  {
    return $this->objectToArray($rawData->toArray());
  }

  private function objectToArray($obj): array
  {
    return json_decode(json_encode($obj), true);
  }

  protected function remap(array $parsedData): array
  {
    $mapping = $this->modelToFill::mapping($this->mappingName);

    $mappedData = array_merge(
      $this->handleOneToOneRemap($mapping, $parsedData),
      $this->handleManyToOneRemap($mapping, $parsedData),
      $this->handleRelationsRemap($mapping, $parsedData),
    );

    return $mappedData;
  }

  private function handleOneToOneRemap(array $mapping, array $data): array
  {
    $remappedData = [];
    foreach ($mapping['oneToOne'] as $srcKey => $distKey) {
      if (!empty($data[$srcKey])) {
        $remappedData[$distKey] = $data[$srcKey];
      }
    }

    return $remappedData;
  }

  private function handleManyToOneRemap(array $mapping, array $data): array
  {
    $remappedData = [];
    foreach ($mapping['manyToOne'] as $srcKey => $distKey) {
      $key = preg_replace('#\.0\.#', '.*.', $srcKey);

      $remappedData[$distKey] = data_get($data, $key);

      if (!is_array($remappedData[$distKey])) {
        $remappedData[$distKey] = [$remappedData[$distKey]];
      }
      
    }

    return $remappedData;
  }

  private function handleRelationsRemap(array $mapping, array $data): array
  {
    $remappedData = [];
    foreach ($mapping['relations'] as $srcKey => $modelClass) {
      $key = preg_replace('#\.0\.#', '.*.', $srcKey);
      $wikidataIds = data_get($data, $key);
      
      if (!is_array($wikidataIds)) {
        $wikidataIds = [$wikidataIds];
      }

      foreach ($wikidataIds as $wikidataId) {
        if (empty($remappedData['relations'])) {
          $remappedData['relations'] = [];
        }
  
        $remappedData['relations'][] = [
          'external_id' => $wikidataId,
          'class' => $modelClass
        ];
      }
    }

    return $remappedData;
  }
}
