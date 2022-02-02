<?php

namespace App\Models\Raw;

use App\Traits\FetchingRegisterable;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class RawDepiction extends Model
{
  use HasFactory;
  use FindableByUniqueKey;
  use FetchingRegisterable;

  protected $guarded = ['id'];
  protected $casts = [
    'aliases' => 'array',
  ];

  function paintings()
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

  public function registerEntry()
  {
    return $this->morphOne(FetchRegister::class, 'registerable');
  }
}
