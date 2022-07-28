from cat import Cat, BadCat, GoodCat


print('good cats go')
cat: Cat = GoodCat()
cat.meow()


print('bad cats go')
cat: Cat = BadCat ()
cat.meow()
