
class cat:
    
    def meow(self):
        print("meow")



class GoodCat(cat):
    def meow(self):
        print("purr purr")


class BadCat(cat):
    def meow(self):
        print("hiss")


c = cat()

c.meow()
