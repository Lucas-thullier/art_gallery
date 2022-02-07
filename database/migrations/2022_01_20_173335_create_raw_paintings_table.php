<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateRawPaintingsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */

    public function up()
    {
        Schema::create('raw_paintings', function (Blueprint $table) {
            $table->id();

            $table->string('name', 500)->nullable();

            $table->integer('source_id');
            $table->string('external_id', 255);

            $table->string('native_name', 500)->nullable();
            $table->tinyText('aliases')->nullable();

            $table->tinyText('title')->nullable();
            $table->string('description', 1000)->nullable();
            $table->text('picture_url')->nullable();
            $table->tinyText('owned_by')->nullable();
            $table->tinyText('inception_at')->nullable();
            $table->tinyText('width')->nullable();
            $table->tinyText('height')->nullable();
            $table->string('described_at', 1000)->nullable();

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
        Schema::dropIfExists('raw_paintings');
    }
}
