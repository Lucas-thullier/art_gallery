<?php

/* Resoudre le soucis d'ambiguite. Ne fait pas du tout la meme chose que les autres extractors. */

namespace App\Imports;

use App\Models\Painting;
use GuzzleHttp\Client;
use Illuminate\Support\Facades\Storage;

class IdWikidataExtractor
{
  public function fullImport()
  {
    // $xmlPaintingsList = $this->getPaintingsListXml();
    $xmlPaintingsList = Storage::disk('public')->get('sparql_test'); //pour test

    $paintingsIds = $this->extractPaintingsId($xmlPaintingsList);

    foreach ($paintingsIds as $paintingId) {
      Painting::firstOrCreate(
        ['wikidata_id' => $paintingId],
        ['wikidata_id' => $paintingId]
      );
    }
  }

  public function getPaintingsListXml(): ?string
  {
    $client = new Client();
    $response = $client->get('https://query.wikidata.org/sparql?query=SELECT%20DISTINCT%20?item%20WHERE%20{%20?item%20p:P31%20?statement0.%20?statement0%20(ps:P31/(wdt:P279*))%20wd:Q3305213.%20}');
    if ($response->getStatusCode() === 200) {
      $xmlPaintingsList = (string) $response->getBody();
      return $xmlPaintingsList;
    } else {
      return null;
    }
  }

  public function extractPaintingsId(string $xmlPaintingsList): array
  {
    $dom = new \DOMDocument();
    $dom->loadXML($xmlPaintingsList);

    $paintingsUrlAsDomList = $dom->getElementsByTagName('uri');

    $paintingsIds = [];
    foreach ($paintingsUrlAsDomList as $paintingUrlAsDomNode) {
      $paintingId = preg_replace('#.+entity\/#', '', $paintingUrlAsDomNode->nodeValue);

      if (trim($paintingId) != '') {
        $paintingsIds[] = $paintingId;
      }
    }

    return $paintingsIds;
  }
}
