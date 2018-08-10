from repository import DogRepository
from repository.sqlalchemy import session
from model import Dog
from repository import PreferencesRepository

class DogService:
    def save_dog(dog_model):
        dog_repository = DogRepository.get_by_name_and_breed(
            dog_model.name,
            dog_model.breed,
        )
        if not dog_repository:
            DogRepository.save(dog_model)


class PreferencesService:
    def save_preferences(user_id, dog_breed):
        preferences = PreferencesRepository(user_id=user_id, dog_breed=dog_breed)
        session.add(preferences)
        session.commit()
