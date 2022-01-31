<?php

use App\Imports\ImportHandlerWikidata;
use App\Imports\WikidataImport;
use App\Models\Artist;
use App\Models\Painting;
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

Route::get('/', function () {
  $paintings = Painting::all();

  foreach ($paintings as $painting) {
    $importHandler = new ImportHandlerWikidata(
      $painting->wikidata_id,
      get_class($painting)
    );

    $preparedData = $importHandler->prepareData();

    $painting->updateOrCreate(
      [
        'wikidata_id' => $painting->wikidata_id
      ],
      $preparedData
    );

    dd($preparedData);
  }

  return view('welcome');
});


// Route::get('/', function () {
//     $t = new ImportHandlerWikidata('Q12418', Painting::class);
//     dd($t->prepareData());
//     return view('welcome');
// });
