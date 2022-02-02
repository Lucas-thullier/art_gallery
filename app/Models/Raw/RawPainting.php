<?php

namespace App\Models\Raw;

use App\Models\Source;
use App\Traits\AdditiveSetter;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class RawPainting extends Model
{
  use HasFactory;
  use FindableByUniqueKey;
  use AdditiveSetter;

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

  public function setAliasesAttribute($value)
  {
    $this->initAdditiveSetter('aliases', $value);
  }

  public function setPictureUrlAttribute($value)
  {
    $this->initAdditiveSetter('picture_url', $value);
  }

  public function setTitleAttribute($value)
  {
    $this->initAdditiveSetter('title', $value);
  }

  public function setOwnedByAttribute($value)
  {
    $this->initAdditiveSetter('owned_by', $value);
  }

  public function setInceptionAtAttribute($value)
  {
    $this->initAdditiveSetter('inception_at', $value);
  }

  public function setWidthAttribute($value)
  {
    $this->initAdditiveSetter('width', $value);
  }

  public function setHeightAttribute($value)
  {
    $this->initAdditiveSetter('height', $value);
  }

  public function setDescribedAtAttribute($value)
  {
    $this->initAdditiveSetter('described_at', $value);
  }

  public static function mapping(string $sourceName): ?array
  {
    $mappings = [
      'wikidata' => [
        'oneToOne' => [
          'label' => 'name',
          'aliases' => 'aliases',
          'description' => 'description',
          'id' => 'external_id'
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
          'properties.P170.values.0.id' => RawArtist::class,
          'properties.P180.values.0.id' => RawDepiction::class,
          'properties.P136.values.0.id' => RawGenre::class,
          'properties.P276.values.0.id' => RawLocation::class,
          'properties.P186.values.0.id' => RawMaterial::class,
          'properties.P135.values.0.id' => RawMovement::class,
        ]
      ]
    ];

    return $mappings[$sourceName] ?? null;
  }

  public function rawArtists()
  {
    return $this->belongsToMany(RawArtist::class);
  }

  public function rawDepictions()
  {
    return $this->belongsToMany(RawDepiction::class);
  }

  public function rawGenres()
  {
    return $this->belongsToMany(RawGenre::class);
  }

  public function rawLocations()
  {
    return $this->belongsToMany(RawLocation::class);
  }

  public function rawMaterials()
  {
    return $this->belongsToMany(RawMaterial::class);
  }

  public function rawMovements()
  {
    return $this->belongsToMany(RawMovement::class);
  }

  public function source()
  {
    return $this->belongsTo(Source::class);
  }
}
