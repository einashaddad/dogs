import unittest
import vcr
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

    @vcr.use_cassette('test/fixtures/spca.yaml', record_mode='new_episodes')
    def test_scrape_spca(self):
        base_url = 'https://www.sfspca.org'
        url = base_url + "/adoptions/dogs"
        dogs = scraper.scrape_spca(url, base_url)
        self.assertEqual(self.domino.name, dogs[0].name)
