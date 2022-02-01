<?php

use App\Imports\ImportHandlerWikidata;
use App\Imports\WikidataImport;
use App\Models\Artist;
use App\Models\Painting;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Date;
use Illuminate\Support\Facades\Route;

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


Route::get('/single', function (Request $request) {
  function import($extractorName, $modelName, $columnName, $uniqueKey)
  {
    switch ($extractorName) { // doit pas etre ici
      case 'App\Extractors\WikidataExtractor':
        $fetchRegisterColumn = 'wikidata_first_fetch';
        $sourceName = 'wikidata';
        break;

      default:
        throw new Exception('Extractor non reconnu : ' . $extractorName);
        break;
    }

    // try {
    $model = $modelName::findByUniqueKey($columnName, $uniqueKey); // devrait devenir resolve existence. Quand y'aura plusieurs sources des doublons vont se créer
    if (is_null($model)) {
      $model = $modelName::create();
    }

    $registerEntry = $model->findFetchEntry();
    if (!$registerEntry->hasAlreadyFetch($fetchRegisterColumn)) {
      $extractor = new $extractorName($uniqueKey, get_class($model));
      $preparedData = $extractor->prepareData();

      $model->update($preparedData);
      $registerEntry->updateFrom($sourceName, $preparedData);
      if (!empty($preparedData['relations'])) {
        foreach ($preparedData['relations'] as $relation) {
          if (!empty($relation['wikidata_id'])) {
            import($extractorName, $relation['class'], $columnName, $relation['wikidata_id']);
          }
        }
      }
    }
  }

  import(
    $request->extractorName,
    $request->modelName,
    $request->columnName,
    $request->uniqueKey
  );


  // } catch (\Throwable $th) {
  //   logger($th);
  // }
});


// Route::get('/', function () {
//     $t = new ImportHandlerWikidata('Q12418', Painting::class);
//     dd($t->prepareData());
//     return view('welcome');
// });
