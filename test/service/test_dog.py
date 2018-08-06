from unittest import TestCase
from unittest.mock import patch

from model import Dog
from repository import DogRepository
from service import DogService

class TestDogService(TestCase):

    dog_model = Dog(**{
        'name': 'Domino',
        'link': 'https://www.sfspca.org/adoptions/pet-details/39286176',
        'image': 'https://www.sfspca.org/sites/default/files/styles/sf_animal_thumb_3col/public/images/animals/39286176-4cf10d31.jpg?itok=V9MiUXS1',
        'age': '2Y 0M',
        'weight': '57lbs. 5oz.',
        'gender': 'Male',
        'breed': 'Border Collie',
    })

    @patch('repository.dog.DogRepository.save')
    @patch('repository.dog.DogRepository.get_by_name_and_breed')
    def test_save_dog_when_dog_doesnt_exist(self, mock_get_by_name_and_breed, mock_save):
        mock_get_by_name_and_breed.return_value = None
        DogService.save_dog(self.dog_model)

        mock_get_by_name_and_breed.assert_called_once_with(
            self.dog_model.name,
            self.dog_model.breed
        )

        mock_save.assert_called_once_with(self.dog_model)

    @patch('repository.dog.DogRepository.save')
    @patch('repository.dog.DogRepository.get_by_name_and_breed')
    def test_save_dog_when_dog_exists(self, mock_get_by_name_and_breed, mock_save):
        mock_get_by_name_and_breed.return_value = True
        DogService.save_dog(self.dog_model)

        mock_get_by_name_and_breed.assert_called_once_with(
            self.dog_model.name,
            self.dog_model.breed
        )

        mock_save.assert_not_called()
