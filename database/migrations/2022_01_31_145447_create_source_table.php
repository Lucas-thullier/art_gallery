<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateSourceTable extends Migration
{
    public function up()
    {
        Schema::create('sources', function (Blueprint $table) {
            $table->id();

            $table->string('extractor', 255)->nullable();
            $table->string('queue', 255)->nullable();
            $table->string('name', 255)->unique();

            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('sources');
    }
}
