<?php

namespace App\Traits;

use Exception;
use App\Models\FetchRegister;
use Illuminate\Database\Eloquent\Relations\MorphOne;

trait FetchingRegisterable
{
  public static function bootFetchingRegisterable()
  {
    static::created(function ($model) {
      FetchRegister::create([
        'registerable_id' => $model->id,
        'registerable_type' => get_class($model)
      ]);
    });
  }

  public function registerEntry(): MorphOne
  {
    return $this->morphOne(FetchRegister::class, 'registerable');
  }

  public function findFetchEntry()
  {
    $fetchEntries = $this->registerEntry()->get();

    if ($fetchEntries->count() < 1) {
      return null;
    } else {
      $model = $fetchEntries[0];

      if ($fetchEntries->count() > 1) {
        throw new Exception('Find multiple fetchEntries for ' . get_class($this) . ' at id :' . $this->id);
      } else {
        return $model;
      }
    }
  }
}
