<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateFetchRegistersTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('fetch_registers', function (Blueprint $table) {
            $table->id();

            $table->integer('registerable_id');
            $table->string('registerable_type', 500);

            $table->dateTime('wikidata_first_fetch', $precision = 0)->nullable();
            $table->dateTime('wikidata_last_update', $precision = 0)->nullable();

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('fetch_registers');
    }
}
