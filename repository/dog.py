from sqlalchemy import Column, Integer, String

from repository import Base
from repository.sqlalchemy import session


class DogRepository(Base):
    __tablename__ = 'dog'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    link = Column(String)
    image = Column(String)
    age = Column(String)
    weight = Column(String)
    gender = Column(String)
    breed = Column(String)

    def __repr__(self):
        return str({
            "name": self.name,
            "link": self.link,
            "image": self.image,
            "age": self.age,
            "weight": self.weight,
            "gender": self.gender,
            "breed": self.breed,
        })

    @classmethod
    def map_from_model(cls, model):
        return DogRepository(
            name=model.name,
            link=model.link,
            image=model.image,
            age=model.age,
            weight=model.weight,
            gender=model.gender,
            breed=model.breed
        )

    @classmethod
    def save(cls, dog_model):
        dog_repo = DogRepository.map_from_model(dog_model)
        session.add(dog_repo)
        session.commit()

    @staticmethod
    def get_by_name_and_breed(name, breed):
        return session.query(DogRepository).filter(
            DogRepository.name == name,
            DogRepository.breed == breed
        ).all()
