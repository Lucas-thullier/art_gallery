<?php

namespace App\Jobs;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use Illuminate\Queue\SerializesModels;
use App\Jobs\Middleware\RateLimited;
use App\Models\Source;

class ExtractionJob implements ShouldQueue
{
  use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

  protected $model;
  public $sourceName;
  public $modelName;
  public $externalId;

  public function __construct($sourceName, $modelName, $externalId)
  {
    $this->sourceName = $sourceName;
    $this->modelName = $modelName;
    $this->externalId = $externalId;
  }

  public function handle()
  {
    $sourceName = $this->sourceName;
    $modelName = $this->modelName;
    $externalId = $this->externalId;

    $source = Source::findByUniqueKey('name', $sourceName);

    if (!is_null($source) && !is_null($source->extractor)) {
      $extractorName = $source->extractor;
      $model = $modelName::findByUniqueKey('external_id', $externalId) ?? new $modelName();

      $extractor = new $extractorName($externalId, get_class($model));
      $preparedData = $extractor->prepareData();
      $preparedData['source_id'] = $source->id;

      $model->fill($preparedData);
      $model->save();

      if (!empty($preparedData['relations'])) {
        foreach ($preparedData['relations'] as $relation) {
          if (!empty($relation['external_id'])) {
            static::dispatch($sourceName, $relation['class'], $relation['external_id'])->onQueue($source->queue);
          }
        }
      }
    }
  }

  public function middleware()
  {
    return [
      new RateLimited
    ];
  }

  public function failed(\Throwable $exception)
  {
    logger($exception);
  }
}
