<?php

namespace App\Jobs;

use App\Imports\ImportHandlerWikidata;
use App\Models\Painting;
use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldBeUnique;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Foundation\Bus\Dispatchable;
use Illuminate\Queue\InteractsWithQueue;
use App\Jobs\Middleware\RateLimited;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Queue\Middleware\WithoutOverlapping;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Redis;
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
  public function __construct(Model $model)
  {
    $this->model = $model;
  }

  /**
   * Execute the job.
   *
   * @return void
   */
  public function handle()
  {
    $importHandler = new ImportHandlerWikidata(
      $this->model->wikidata_id,
      get_class($this->model)
    );

    $preparedData = $importHandler->prepareData();

    $this->model->updateOrCreate(
      [
        'wikidata_id' => $this->model->wikidata_id
      ],
      $preparedData
    );

    logger($this->model);
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
