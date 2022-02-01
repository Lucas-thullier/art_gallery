<?php

namespace App\Traits;

use Exception;

trait FindableByUniqueKey
{
  public static function findByUniqueKey(string $columnName, string $uniqueKey)
  {
    $collection = static::where($columnName, $uniqueKey)->get();

    if ($collection->count() < 1) {
      return null;
    } else {
      $model = $collection[0];

      if ($collection->count() > 1) {
        throw new Exception('Missing unique key constraint for wikidata_id on ' . get_class($model));
      } else {
        return $model;
      }
    }
  }
}
