<?php

use App\Imports\ImportHandlerWikidata;
use App\Models\Painting;
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

// Route::get('/', function () {
//     $t = new App\Imports\WikidataImport();
//     dd($t->fullImport());
//     return view('welcome');
// });


Route::get('/', function () {
    $t = new ImportHandlerWikidata('Q12418', Painting::class);
    dd($t->prepareData());
    return view('welcome');
});
