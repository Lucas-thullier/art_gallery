<?php

namespace App\Jobs;

use App\Extractors\IdWikidataExtractor;
use App\Imports\ImportHandlerWikidata;
use App\Models\Painting;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldBeUnique;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use App\Jobs\Middleware\RateLimited;
use App\Models\Source;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Queue\Middleware\WithoutOverlapping;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Redis;
use Illuminate\Support\Facades\Storage;
use Wikidata\Wikidata;

class FillPaintingData implements ShouldQueue
{
  use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

  protected $model;

  /**
   * Create a new job instance.
   *
   * @return void
   */
  public $sourceName;
  public $modelName;
  public $externalId;
  public function __construct($sourceName, $modelName, $externalId)
  {
    $this->sourceName = $sourceName;
    $this->modelName = $modelName;
    $this->externalId = $externalId;
  }

  /**
   * Execute the job.
   *
   * @return void
   */
  public function handle()
  {
    // try {
    //   $t = new IdWikidataExtractor();
    //   $t = $t->extract();
    //   Storage::put('test.json', json_encode($t));
    // } catch (\Throwable $th) {
    //   logger($th);
    // }
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
            FillPaintingData::dispatch($sourceName, $relation['class'], $relation['external_id']);
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
