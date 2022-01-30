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
use Illuminate\Queue\Middleware\WithoutOverlapping;
use Illuminate\Queue\SerializesModels;
use Illuminate\Support\Facades\Redis;
use Wikidata\Wikidata;

class FillPaintingData implements ShouldQueue
{
  use Dispatchable, InteractsWithQueue, Queueable, SerializesModels;

  protected $painting;

  /**
   * Create a new job instance.
   *
   * @return void
   */
  public function __construct(Painting $painting)
  {
    $this->painting = $painting;
  }

  /**
   * Execute the job.
   *
   * @return void
   */
  public function handle()
  {
    $importHandler = new ImportHandlerWikidata(
      $this->painting->wikidata_id,
      Painting::class
    );

    $preparedData = $importHandler->prepareData();
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
