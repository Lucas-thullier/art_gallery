<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePaintingsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('paintings', function (Blueprint $table) {
            $table->id();

            $table->string('name', 500);
            $table->string('native_name', 500);
            $table->string('wikidata_url', 500)->unique();

            $table->string('title', 500);
            $table->string('picture_url', 500);
            $table->string('owned_by', 500);
            $table->string('inception_at', 500);
            $table->unsignedInteger('width');
            $table->unsignedInteger('height');
            $table->string('described_at', 500);

            $table->softDeletes($column = 'deleted_at', $precision = 0);

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
        Schema::dropIfExists('paintings');
    }
}
