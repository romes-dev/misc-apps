# Classe Mãe
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def move(self):
        pass

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Primeira Classe Filha
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name} barks.")

    def move(self):
        print(f"{self.name} is running.")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Segunda Classe Filha
class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species

    def make_sound(self):
        print(f"{self.name} chirps.")

    def move(self):
        print(f"{self.name} is flying.")

    def build_nest(self):
        print(f"{self.name} is building a nest.")

# Exemplo de uso
if __name__ == "__main__":
    caramelo = Dog("Totó", "Vira-lata")
    bird = Bird("Tweety", "Canary")

    caramelo.make_sound()  # Buddy barks.
    caramelo.move()        # Buddy is running.
    caramelo.fetch()       # Buddy is fetching the ball.
    caramelo.sleep()       # Buddy is sleeping.

    bird.make_sound() # Tweety chirps.
    bird.move()       # Tweety is flying.
    bird.build_nest() # Tweety is building a nest.
    bird.sleep()      # Tweety is sleeping.
