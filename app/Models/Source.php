<?php

namespace App\Models;

use App\Models\Raw\RawArtist;
use App\Models\Raw\RawDepiction;
use App\Models\Raw\RawGenre;
use App\Models\Raw\RawLocation;
use App\Models\Raw\RawMaterial;
use App\Models\Raw\RawMovement;
use App\Models\Raw\RawPainting;
use App\Traits\FindableByUniqueKey;
use Illuminate\Database\Eloquent\Model;

class Source extends Model
{
  use FindableByUniqueKey;
  
  protected $guarded  = ['id'];

  public function rawPaintings()
  {
    return $this->hasMany(RawPainting::class);
  }

  public function rawArtists()
  {
    return $this->hasMany(RawArtist::class);
  }

  public function rawDepictions()
  {
    return $this->hasMany(RawDepiction::class);
  }

  public function rawGenres()
  {
    return $this->hasMany(RawGenre::class);
  }

  public function rawLocations()
  {
    return $this->hasMany(RawLocation::class);
  }

  public function rawMaterials()
  {
    return $this->hasMany(RawMaterial::class);
  }

  public function rawMovements()
  {
    return $this->hasMany(RawMovement::class);
  }
}
