<?php

namespace App\Models;

use App\Jobs\FillPaintingData;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Painting extends Model
{
  use HasFactory;

  protected $guarded = ['id'];
  protected $casts = [
    'aliases' => 'array'
  ];

  protected static function booted()
  {
    static::created(function ($painting) {
      if (
        !empty($painting->wikidata_id)
        && empty($painting->name)
        && empty($painting->picture_url)
      ) {
        FillPaintingData::dispatch($painting);
      }
    });
  }

  public static function mapping(string $distName): ?array
  {
    $mappings = [
      'wikidata' => [
        'oneToOne' => [
          'label' => 'name',
          'aliases' => 'aliases',
          'description' => 'description',
        ],
        'manyToOne' => [
          'properties.P18.values.0.label'  => 'picture_url',
          'properties.P1476.values.0.label' => 'title',
          'properties.P127.values.0.label' => 'owned_by',
          'properties.P571.values.0.label' => 'inception_at',
          'properties.P2049.values.0.label' => 'width',
          'properties.P2048.values.0.label' => 'height',
          'properties.P973.values.0.label' => 'described_at'
        ]
      ]
    ];

    return $mappings[$distName] ?? null;
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
