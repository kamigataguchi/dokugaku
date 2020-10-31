class Horse:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

sadayuki = Rider("kamigataguchi")
kafka = Horse("kafka", "red", sadayuki)
print(kafka.owner.name)