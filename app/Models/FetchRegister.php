<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Support\Facades\Date;

class FetchRegister extends Model
{
  use HasFactory;

  protected $guarded = ['id'];

  public function registerable()
  {
    return $this->morphTo();
  }

  public function hasAlreadyFetch(string $columnName): bool
  {
    if (empty($this->$columnName)) {
      return false;
    } else {
      return true;
    }
  }

  public function updateFrom(string $source)
  {
    switch ($source) {
      case 'wikidata':
        $data = [
          'wikidata_first_fetch' => $this->wikidata_first_fetch ?? Date::now(),
          'wikidata_last_update' => Date::now(),
        ];
        break;
      default:
        break;
    }

    $this->update($data);
  }
}
