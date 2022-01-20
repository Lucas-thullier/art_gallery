<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Painting extends Model
{
    use HasFactory;

    function artists()
    {
        return $this->belongsToMany(Artist::class);
    }

    function depictions()
    {
        return $this->belongsToMany(Depiction::class);
    }

    function genres()
    {
        return $this->belongsToMany(Genre::class);
    }

    function locations()
    {
        return $this->belongsToMany(Location::class);
    }

    function materials()
    {
        return $this->belongsToMany(Material::class);
    }

    function movements()
    {
        return $this->belongsToMany(Movement::class);
    }
}
