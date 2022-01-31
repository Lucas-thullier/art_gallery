<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class FetchRegister extends Model
{
  use HasFactory;

  protected $guarded = ['id'];

  public function registerable()
  {
    return $this->morphTo();
  }

  public function hasAlreadyFetchWikidata(): bool
  {
    if (empty($this->wikidata_first_fetch)) {
      return false;
    } else {
      return true;
    }
  }
}
