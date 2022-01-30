<?php

namespace App\Imports;

abstract class AbstractImportHandler
{
  protected string $sourceId;
  protected array $mappedContent;
  protected string $mappingName; # abstract
  protected $modelToFill;

  public function __construct(string $sourceId, string $modelToFill)
  {
    $this->sourceId = $sourceId;
    $this->modelToFill = $modelToFill;
  }

  public function prepareData(): ?array
  {
    $this->connection();

    $rawData = $this->fetch($this->sourceId);
    $parsedData = $this->parse($rawData);

    if (count($parsedData) > 0) {
      $this->mappedContent = $this->remap($parsedData);
      return $this->mappedContent;
    } else {
      return null;
    }
  }

  abstract protected function connection();
  abstract protected function fetch();
  abstract protected function parse($rawData): array;
  abstract protected function remap(array $parsedData);
}
