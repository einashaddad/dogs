class Dog:
    def __init__(self, name, link, image):
        self.name = name
        self.link = link
        self.image = image
        self.age = None
        self.weight = None
        self.gender = None
        self.breed = None

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
