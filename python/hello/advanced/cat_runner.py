from cat import Cat, BadCat, GoodCat, VeryBadCat, cat_cage


print("very bad cats need cages")

cat1: Cat = GoodCat()
cat2: Cat = BadCat()
cat3: Cat = VeryBadCat()


@cat_cage
def run_in_cage():
    cat1.meow()
    cat2.meow()
    cat3.meow()


run_in_cage()
