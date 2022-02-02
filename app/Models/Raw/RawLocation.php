<?php

namespace App\Models\Raw;

use App\Models\Source;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class RawLocation extends Model
{
  use HasFactory;
  use FindableByUniqueKey;

  protected $guarded = ['id'];
  protected $casts = [
    'aliases' => 'array',
  ];

  function rawPaintings()
  {
    return $this->belongsToMany(RawPainting::class);
  }

  public static function mapping(string $sourceName): ?array
  {
    $mappings = [
      'wikidata' => [
        'oneToOne' => [
          'id' => 'external_id',
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

  public function source()
  {
    return $this->belongsTo(Source::class);
  }
}
