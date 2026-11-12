class Dinosaur:
    def __init__(self, name, species, diet, age):
        self.name = name
        self.species = species
        self.diet = diet
        self.age = age

    def roar(self):
        return f"{self.name} lets out a mighty ROAR!"

    def eat(self, food):
        if food in self.diet:
            return f"{self.name} happily eats the {food}."
        return f"{self.name} doesn't eat {food}."

    def dino_info(self):
        foods = ", ".join(self.diet)
        return (
            f"Name: {self.name}, Species: {self.species}, "
            f"Diet: {foods}, Age: {self.age}"
        )


if __name__ == "__main__":
    dinosaurs = [
        Dinosaur("Rex", "Tyrannosaurus rex", ["meat"], 12),
        Dinosaur("Pickle", "Triceratops", ["onions", "turnips"], 8),
        Dinosaur("sky", "Pteranodon", ["fish"], 5),
    ]

    for dino in dinosaurs:
        print(dino.dino_info())
        print(dino.roar())
        print(dino.eat(dino.diet[0]))
        print(dino.eat("candy"))
        print()