def metricConversion(value, units):
    if units == "pounds":
        z = value * .4536
        return z
    elif units == "kilos":
        a = value * 2.2046
        return a
    elif units == "ounces":
        b = value * 28.3495
        return b
    elif units == "grams":
        c = value * .0353
        return c
    elif units == "miles":
        d = value * 1.6093
        return d
    elif units == "kilometers":
        e = value * 0.6214
        return e
    elif units == "inches":
        f = value * 2.54
        return f
    elif units == "centimeters":
        g = value * .3937
        return g
    else:
        print(value, units, "is not a valid unit")
def main():
    value = float(input("Enter value: "))
    units = input("Enter units: ")
    x = metricConversion(value, units)
    print("{:.4f}".format(x))
main()
