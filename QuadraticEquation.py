
def QuadraticEquation():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    delta = b*b-4*a*c

    if delta > 0:
        sqrt_delta = math.sqrt(delta)
        x_one = (-b -sqrt_delta) / (2*a)
        x_two = (-b +sqrt_delta) / (2*a)
        print(f"x1 = {x_one}")
        print(f"x2 = {x_two}")

    elif delta == 0:
        x_one = x_two = -b/ (2*a)
        print (f"x1 is equal to x2 = {x_one}")

    elif delta < 0:
        print("There are no real results ")

QuadraticEquation()