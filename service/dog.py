from repository import DogRepository
from model import Dog

class DogService:
    def save_dog(dog_model):
        dog_repository = DogRepository.get_by_name_and_breed(
            dog_model.name,
            dog_model.breed,
        )
        if not dog_repository:
            DogRepository.save(dog_model)
