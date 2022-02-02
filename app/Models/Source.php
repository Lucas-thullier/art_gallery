<?php

namespace App\Models;

use App\Models\Raw\FetchRegister;
use Illuminate\Database\Eloquent\Model;

class Source extends Model
{
  protected $guarded  = ['id'];

  public function fetchEntries()
  {
    return $this->hasMany(FetchRegister::class);
  }
}
