<?php

use App\Traits\Migrations\HasMinimalWikidataRecord;
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreatePaintingsTable extends Migration
{
    use HasMinimalWikidataRecord;

    /**
     * Run the migrations.
     *
     * @return void
     */

    public function up()
    {
        Schema::create('paintings', function (Blueprint $table) {
            $table->id();

            $this->createMinimalWikidataColumn($table);

            $table->string('native_name', 500)->nullable();
            $table->string('aliases', 1000)->nullable();

            $table->string('title', 500)->nullable();
            $table->string('description', 1000)->nullable();
            $table->string('picture_url', 500)->nullable();
            $table->string('owned_by', 500)->nullable();
            $table->string('inception_at', 500)->nullable();
            $table->string('width', 1000)->nullable();
            $table->string('height', 1000)->nullable();
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
        Schema::dropIfExists('paintings');
    }
}
