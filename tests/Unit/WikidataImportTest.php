<?php

namespace Tests\Unit;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;
use App\Imports\WikidataImport;

class WikidataImportTest extends TestCase
{
  protected $wikidataImport;

  public function setUp(): void
  {
    $this->wikidataImport = new WikidataImport();
  }

  public function test_getPaintingsListXml()
  {
    $paintingsList = $this->wikidataImport->getPaintingsListXml();

    $this->assertIsString($paintingsList) || $this->isNull($paintingsList);

    return $paintingsList;
  }

  /**
   * @depends test_getPaintingsListXml
   * 
   */
  public function test_extractPaintingsId(string $paintingsList)
  {
    $paintingsList = $this->wikidataImport->extractPaintingsId($paintingsList);
    dd($paintingsList);

    $this->assertIsArray($paintingsList);
  }
}
