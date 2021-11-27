from django.test import TestCase
from django.urls import reverse

from .models import Artwork, Author

class ArtworksIndexViewTests(TestCase):
    def test_no_artworks(self):
        response = self.client.get(reverse('gallery:index'))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aucune peinture disponible")
    
class ArtworksDetailsViewTests(TestCase):
    def test_have_artwork(self):
        author = Author.objects.create(
            main_picture_url = 'url',
            biography = 'blalb',
            created_at = '2021-01-01',
            updated_at = '2021-01-01'
        )

        artwork = Artwork.objects.create(
            url = 'url',
            description = 'blabla',
            author = author,
            width = '1',
            height = '1',
            publication_date = '2021-01-01',
            created_at = '2021-01-01',
            updated_at = '2021-01-01'
        )
        response = self.client.get(reverse('gallery:detail', args=(artwork.id,)))
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, artwork.description)