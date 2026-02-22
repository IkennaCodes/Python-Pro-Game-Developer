class Dog():
    legs = 4
    skin = "fluffy"
    breed = True
    eyes = 2
    ears = 2
    can_fly = False

    def bark(self):
        print("Woof Woof!")

    def play(self):
        print("The dog plays a lot")

golden_ret = Dog()
husky = Dog()
poodle = Dog()

print("The husky has", husky.eyes , "eyes")
poodle.bark()
