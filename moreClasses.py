class Cat():
    legs = 4
    tail = True
    fur = "soft"
    eyes = 2
    can_swim = False

    def meow(self):
        print("Meow Meow!")

    def sleep(self):
        print("The cat is sleeping.")


class Bird():
    legs = 2
    wings = 2
    can_fly = True
    beak = True
    feathers = True

    def chirp(self):
        print("Chirp Chirp!")

    def fly(self):
        print("The bird is flying.")


# objects
persian = Cat()
siamese = Cat()

parrot = Bird()
eagle = Bird()


print("The eagle has", eagle.wings, "wings")
persian.meow()
parrot.fly()