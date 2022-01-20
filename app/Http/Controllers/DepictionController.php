<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreDepictionRequest;
use App\Http\Requests\UpdateDepictionRequest;
use App\Models\Depiction;

class DepictionController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \App\Http\Requests\StoreDepictionRequest  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreDepictionRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Depiction  $depiction
     * @return \Illuminate\Http\Response
     */
    public function show(Depiction $depiction)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Depiction  $depiction
     * @return \Illuminate\Http\Response
     */
    public function edit(Depiction $depiction)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \App\Http\Requests\UpdateDepictionRequest  $request
     * @param  \App\Models\Depiction  $depiction
     * @return \Illuminate\Http\Response
     */
    public function update(UpdateDepictionRequest $request, Depiction $depiction)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Depiction  $depiction
     * @return \Illuminate\Http\Response
     */
    public function destroy(Depiction $depiction)
    {
        //
    }
}
