def first_function(name, place):
    print(f"Hello {name} how is {place}!")


def total_calc(bill_amount, tip_perc=10):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")


first_function(name="Asad", place="Paris")
total_calc(150)
