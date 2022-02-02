<?php

namespace App\Models\Raw;

use App\Traits\FetchingRegisterable;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class RawArtist extends Model
{
  use HasFactory;
  use FindableByUniqueKey;
  use FetchingRegisterable;

  protected $guarded  = ['id'];

  public function paintings()
  {
    return $this->belongsToMany(Painting::class);
  }

  public static function mapping(string $sourceName): ?array
  {
    $mappings = [
      'wikidata' => [
        'oneToOne' => [
          'id' => 'wikidata_id',
          'label' => 'name',
          'aliases' => 'aliases',
          'description' => 'description',
        ],
        'manyToOne' => [],
        'relations' => []
      ]
    ];

    return $mappings[$sourceName] ?? null;
  }
}
