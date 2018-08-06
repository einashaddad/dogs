class Dog:
    def __init__(
        self,
        name=None,
        link=None,
        image=None,
        age=None,
        weight=None,
        gender=None,
        breed=None,
    ):
        self.name = name
        self.link = link
        self.image = image
        self.age = age
        self.weight = weight
        self.gender = gender
        self.breed = breed

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
