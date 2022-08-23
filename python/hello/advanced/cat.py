def cat_cage(func):
    def exception_handler(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as error:
            print(f"Cat was bad: {error} No harm was done due to Cage")

    return exception_handler


class Cat:
    def __init__(cat):
        cat = cat

    def meow(self):
        print("Meow")


class GoodCat(Cat):
    @cat_cage
    def meow(self):
        print("Purr purr Meow")


class BadCat(Cat):
    @cat_cage
    def meow(self):
        print("Hiss")


class VeryBadCat(Cat):
    @cat_cage
    def meow(self):
        raise Exception("Nope, Scratch scratch")
