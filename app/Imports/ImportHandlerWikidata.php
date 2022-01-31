<?php

namespace App\Imports;

use App\Imports\AbstractImportHandler;
use Wikidata\Wikidata;

class ImportHandlerWikidata extends AbstractImportHandler
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
      $key = preg_replace('#.0.#', '.*.', $srcKey);
      $mappedData[$distKey] = data_get($data, $key);
    }

    return $remappedData;
  }

  private function handleRelationsRemap(array $mapping, array $data): array
  {
    $remappedData = [];
    foreach ($mapping['relations'] as $srcKey => $modelClass) {
      $wikidata_id = data_get($data, $srcKey);
      $relationModel = $modelClass::firstOrCreate(['wikidata_id' => $wikidata_id]);

      if (empty($relationModel->registerEntry()->first()) || !$relationModel->registerEntry()->first()->hasAlreadyFetchWikidata()) {
        $importHandler = new ImportHandlerWikidata(
          $relationModel->wikidata_id,
          get_class($relationModel)
        );

        if (empty($remappedData['relations'])) {
          $remappedData['relations'] = [];
        }

        $remappedData['relations'][] = [
          'data' => $importHandler->prepareData(),
          'class' => get_class($relationModel)
        ];
      }
    }

    return $remappedData;
  }

  private function objectToArray($obj): array
  {
    return json_decode(json_encode($obj), true);
  }
}
