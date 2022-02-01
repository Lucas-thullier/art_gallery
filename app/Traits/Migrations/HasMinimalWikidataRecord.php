<?php

namespace App\Traits\Migrations;

use Illuminate\Database\Schema\Blueprint;

trait HasMinimalWikidataRecord
{
  protected function createMinimalWikidataColumn(Blueprint &$table)
  {
    $table->string('name', 500)->nullable();
    $table->string('wikidata_id', 50)->nullable()->unique();
  }
}
