<?php

use App\Jobs\ExtractionJob;
use App\Models\Raw\RawPainting;
use App\Models\Source;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Redis;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Storage;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function (Request $request) {
  $sourceName = $request->source;
  $modelName = $request->model;

  $source = Source::findByUniqueKey('name', $sourceName);

  $ids = json_decode(Storage::get('test.json'));
  foreach ($ids as $id) {
    ExtractionJob::dispatch($sourceName, $modelName, $id)->onQueue($source->queue);
  }
});

Route::get('/redis', function (Request $request) {
  Redis::command('flushdb');
});
