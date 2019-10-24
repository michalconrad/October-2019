def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


print('This program solves equation ax^2+bx+c = 0')
print('Enter the values for a, b and c:')

a = input("a = ")
b = input("b = ")
c = input("c = ")

if not (check_int(a) and check_int(b) and check_int(c)):
    print("a, b and c need to be int!")

else:
    a = int(a)
    b = int(b)
    c = int(c)

    if a == 0:
        print("a cannot be a 0!")
    else:
        delta = b**2 - 4*a*c

        if delta < 0:
            print("there is no solution")
        elif delta == 0:
            x1 = -b/(2*a)
            print(f"there is one solution: {x1}")
        else:
            x1 = (-b-delta**0.5)/(2*a)
            x2 = (-b+delta**0.5)/(2*a)
            print(f"there are two solutions: {x1} and {x2}")
