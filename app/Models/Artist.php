<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Artist extends Model
{
  use HasFactory;

  protected $guarded  = ['id'];

  public function paintings()
  {
    return $this->belongsToMany(Painting::class);
  }

  public function registerEntry()
  {
    return $this->morphOne(FetchRegister::class, 'registerable');
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
          //   'properties.P18.values.0.label'  => 'picture_url',
          //   'properties.P1476.values.0.label' => 'title',
          //   'properties.P127.values.0.label' => 'owned_by',
          //   'properties.P571.values.0.label' => 'inception_at',
          //   'properties.P2049.values.0.label' => 'width',
          //   'properties.P2048.values.0.label' => 'height',
          //   'properties.P973.values.0.label' => 'described_at'
        ],
        'relations' => [
          //   // 'properties.P170.values.0.id' => Artist::class,
          //   // 'properties.P180.values.0.id' => Depiction::class,
          //   // 'properties.P136.values.0.id' => Genre::class,
          //   // 'properties.P276.values.0.id' => Location::class,
          //   // 'properties.P186.values.0.id' => Material::class,
          //   // 'properties.P135.values.0.id' => Movement::class,
        ]
      ]
    ];

    return $mappings[$distName] ?? null;
  }
}
