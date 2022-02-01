<?php

namespace App\Models;

use App\Traits\FetchingRegisterable;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Painting extends Model
{
  use HasFactory;
  use FindableByUniqueKey;
  use FetchingRegisterable;

  protected static function boot()
  {
    parent::boot();
  }

  protected $guarded = ['id'];
  protected $casts = [
    'aliases' => 'array',
    'picture_url' => 'array',
    'title' => 'array',
    'owned_by' => 'array',
    'inception_at' => 'array',
    'width' => 'array',
    'height' => 'array',
    'described_at' => 'array',
  ];

  public static function mapping(string $sourceName): ?array
  {
    $mappings = [
      'wikidata' => [
        'oneToOne' => [
          'label' => 'name',
          'aliases' => 'aliases',
          'description' => 'description',
          'id' => 'wikidata_id'
        ],
        'manyToOne' => [
          'properties.P18.values.0.label'  => 'picture_url',
          'properties.P1476.values.0.label' => 'title',
          'properties.P127.values.0.label' => 'owned_by',
          'properties.P571.values.0.label' => 'inception_at',
          'properties.P2049.values.0.label' => 'width',
          'properties.P2048.values.0.label' => 'height',
          'properties.P973.values.0.label' => 'described_at'
        ],
        'relations' => [
          'properties.P170.values.0.id' => Artist::class,
          'properties.P180.values.0.id' => Depiction::class,
          'properties.P136.values.0.id' => Genre::class,
          'properties.P276.values.0.id' => Location::class,
          'properties.P186.values.0.id' => Material::class,
          'properties.P135.values.0.id' => Movement::class,
        ]
      ]
    ];

    return $mappings[$sourceName] ?? null;
  }

  public function artists()
  {
    return $this->belongsToMany(Artist::class);
  }

  public function depictions()
  {
    return $this->belongsToMany(Depiction::class);
  }

  public function genres()
  {
    return $this->belongsToMany(Genre::class);
  }

  public function locations()
  {
    return $this->belongsToMany(Location::class);
  }

  public function materials()
  {
    return $this->belongsToMany(Material::class);
  }

  public function movements()
  {
    return $this->belongsToMany(Movement::class);
  }
}
