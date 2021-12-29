from django.test import TestCase
from django.urls import reverse

from .models import Painting, Creator


# class ArtworksIndexViewTests(TestCase):
#     def test_no_artworks(self):
#         response = self.client.get(reverse('gallery:index'))

#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Aucune peinture disponible")


# class ArtworksDetailsViewTests(TestCase):
#     def test_have_artwork(self):
#         author = Author.objects.create(
#             main_picture_url='url',
#             biography='blalb',
#             created_at='2021-01-01',
#             updated_at='2021-01-01'
#         )

#         artwork = Artwork.objects.create(
#             url='url',
#             description='blabla',
#             author=author,
#             width='1',
#             height='1',
#             publication_date='2021-01-01',
#             created_at='2021-01-01',
#             updated_at='2021-01-01'
#         )
#         response = self.client.get(
#             reverse('gallery:detail', args=(artwork.id,)))

#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, artwork.description)


class PaintingModelCreationTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.painting = Painting.objects.create(
            name="test name",
            wikidata_url='url',
            inception_at='2021-01-01',
            width='1',
            height='1',
            created_at='2021-01-01',
            updated_at='2021-01-01'
        )

    def test_well_formatted_creation(self):
        painting = self.painting

        self.assertIsInstance(painting, Painting)

    def test_url_at_inception_date(self):
        painting = self.painting
        painting.inception_at = 'http://test.fr'
        painting.save()

        self.assertIsNone(painting.inception_at)

    # def test_bad_inception_at(self):
    #     painting = Painting.objects.create(
    #         name="test name",
    #         wikidata_url='url',
    #         inception_at='http://test.fr',
    #         width='1',
    #         height='1',
    #         created_at='2021-01-01',
    #         updated_at='2021-01-01'
    #     )

    #     self.assertIsInstance(painting, Painting)
    #     self.assertIsNone(painting.inception_at)
