<?php

namespace App\Imports;

use Wikidata\Wikidata;
use App\Imports\AbstractImportHandler;
use Illuminate\Support\Arr;

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
    // logger($rawData->toArray());
    return $rawData->toArray();
  }

  protected function remap(array $parsedData): array
  {
    $mapping = $this->modelToFill::mapping($this->mappingName);
    // dd($dottedMapping, $dottedData);

    $mappedData = [];

    foreach ($mapping['oneToOne'] as $srcKey => $distKey) {
      if (!empty($parsedData[$srcKey])) {
        $mappedData[$distKey] = $parsedData[$srcKey];
      }
    }

    $manyToOneDottedMapping = $mapping['manyToOne'];
    $arrayedData = $this->objectToArray($parsedData);
    dd(Arr::dot($arrayedData));
    foreach ($manyToOneDottedMapping as $srcKey => $distKey) {
      $key = preg_replace('#.0.#', '.*.', $srcKey);
      $mappedData[$distKey] = data_get($arrayedData, $key);
    }

    dd($mappedData);
    return $mappedData;
  }

  private function objectToArray($obj)
  {
    return json_decode(json_encode($obj), true);
  }
}
