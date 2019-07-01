for i in range(1, 101):
    str_out = ""

    div_three = i % 3 == 0
    div_five = i % 5 == 0

    if div_three:
        str_out += "fizz"

    if div_five:
        str_out += "buzz"

    if (not div_three) and (not div_five):
        str_out += str(i)

    print(str_out)
