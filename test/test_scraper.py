import unittest
from unittest.mock import patch, Mock

import scraper
from model import Dog


class TestScraper(unittest.TestCase):

    domino = Dog(**{
        'name': 'Domino',
        'link': 'https://www.sfspca.org/adoptions/pet-details/39286176',
        'image': 'https://www.sfspca.org/sites/default/files/styles/sf_animal_thumb_3col/public/images/animals/39286176-4cf10d31.jpg?itok=V9MiUXS1',
        'age': '2Y 0M',
        'weight': '57lbs. 5oz.',
        'gender': 'Male',
        'breed': 'Border Collie',
    })

    class Request():
        def __init__(self):
            self.text = None

    def setUp(self):

        with open('test/fixtures/spca_fixture.html') as f:
            self.spca_fixture = self.Request()
            self.spca_fixture.text = f.read()

        with open('test/fixtures/dog_fixture.html') as f:
            self.dog_fixture = self.Request()
            self.dog_fixture.text = f.read()

    @patch('requests.get')
    def test_scrape_spca(self, mock_get):
        def side_effect(*args):
            def second_call(*args):
                return self.dog_fixture
            mock_get.side_effect = second_call
            return self.spca_fixture

        mock_get.side_effect = side_effect
        dogs = scraper.scrape_spca('url', 'https://www.sfspca.org')
        self.assertEqual(self.domino.name, dogs[0].name)
