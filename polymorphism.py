class Dogs:
    def size(self):
        print("Different typoes of dogs can have a variety of sizes.")
class Husky(Dogs):
    dog = "Husky"
    
    def size(self):
        print("{}'s are big dogs.".format(self.dog))
class Corgi(Dogs):
    dog = "Corgi"
    
    def size(self):
        print("{}'s are small dogs.".format(self.dog))

obj_dogs = Dogs()
obj_husky = Husky()
obj_corgi = Corgi()

obj_dogs.size()
obj_husky.size()
obj_corgi.size()
