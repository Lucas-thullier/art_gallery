<?php

use App\Extractors\IdWikidataExtractor;
use App\Jobs\FillPaintingData;
use App\Models\Raw\RawArtist;
use App\Models\Raw\RawPainting;
use App\Models\Source;
use Illuminate\Http\Request;
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


// Route::get('/single', function (Request $request) {
//   function import($sourceName, $modelName, $externalId)
//   {
//     $source = Source::findByUniqueKey('name', $sourceName);

//     if (!is_null($source) && !is_null($source->extractor)) {
//       $extractorName = $source->extractor;
//       $model = $modelName::findByUniqueKey('external_id', $externalId) ?? new $modelName();

//       $extractor = new $extractorName($externalId, get_class($model));
//       $preparedData = $extractor->prepareData();
//       $preparedData['source_id'] = $source->id;

//       $model->fill($preparedData);
//       $model->save();

//       if (!empty($preparedData['relations'])) {
//         foreach ($preparedData['relations'] as $relation) {
//           if (!empty($relation['external_id'])) {
//             import($sourceName, $relation['class'], $relation['external_id']);
//           }
//         }
//       }
//     }
//   }

//   import(
//     $request->source,
//     $request->model,
//     $request->externalId
//   );
// });

Route::get('/single', function (Request $request) {
  $sourceName = $request->source;
  $modelName = $request->model;
  $externalId = $request->externalId;

  $ids = json_decode(Storage::get('test.json'));
  foreach ($ids as $id) {
    FillPaintingData::dispatch($sourceName, $modelName, $id);
    // break;
  }
});


Route::get('/', function () {
  // RawPainting::updateOrCreate(['id' => 13], [
  //   'source_id' => '1',
  //   'external_id' => '1',
  //   'picture_url' => ['test', 'test'],
  //   'aliases' => ['test', 'test'],
  //   'title' => ['test', 'test'],
  //   'owned_by' => ['test', 'test'],
  //   'inception_at' => ['test', 'test'],
  //   'width' => ['test', 'test'],
  //   'height' => ['test', 'test'],
  //   'described_at' => ['test', 'test'],
  // ]);

  Storage::disk('local')->put('test.json', 'content');
  // $t = RawPainting::find(12);
  // $t->fill(['picture_url' => ['blabla', 'blabla']]);
  // $t->save();
});
