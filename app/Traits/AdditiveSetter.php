<?php

namespace App\Traits;

trait AdditiveSetter
{
  public function initAdditiveSetter(string $fieldName, $value)
  {
    $mergedData = array_merge($this->$fieldName ?? [], $value);
    $serializedData = json_encode($mergedData);
    $this->attributes[$fieldName] = $serializedData;
  }
}
