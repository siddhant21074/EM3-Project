import sympy as sp
import math

# Defining Symbols

x, y, z = sp.symbols("x y z")
i, j, k = sp.symbols("i, j, k")


def along_the_vector():
    print("Enter the vectors field:")
    vec1 = int(input("i = "))
    vec2 = int(input("j = "))
    vec3 = int(input("k = "))

    eqn1 = wrt_x.subs(x, pt1)
    eqn2 = wrt_y.subs(y, pt2)
    eqn3 = wrt_z.subs(z, pt3)

    dd = ((eqn1 * vec1 + eqn2 * vec2 + eqn3 * vec3) /
          (sp.sqrt((vec1 ** 2 + vec2 ** 2 + vec3 ** 2))))

    print(sp.simplify(dd))

    print(sp.simplify(float(dd)))


def toward_the_point():
    print("Enter the points toward which you want to find D.D:")
    toward_pt1 = int(input("Point 1: "))
    toward_pt2 = int(input("Point 2: "))
    toward_pt3 = int(input("Point 3: "))

    eqn1 = wrt_x.subs(x, pt1)
    eqn2 = wrt_y.subs(y, pt2)
    eqn3 = wrt_z.subs(z, pt3)

    a_b_bar1 = toward_pt1 - pt1
    a_b_bar2 = toward_pt2 - pt2
    a_b_bar3 = toward_pt3 - pt3

    dd = (eqn1 * a_b_bar1 + eqn2 * a_b_bar2 + eqn3 * a_b_bar3) / (
        sp.sqrt((a_b_bar1 ** 2 + a_b_bar2 ** 2 + a_b_bar3 ** 2)))

    print(sp.simplify(dd))

    print(sp.simplify(float(dd)))


def normal_to_surface():
    t1 = wrt_x.subs(x, pt1)
    t2 = wrt_y.subs(y, pt2)
    t3 = wrt_z.subs(z, pt3)
    term = t1 + t2 + t3

    print(term)

    second_eqn = input("Enter the second equation: ")

    p1 = int(input("Point 1: "))
    p2 = int(input("Point 2: "))
    p3 = int(input("Point 3: "))

    wrt_x1 = sp.diff(second_eqn, x)
    wrt_y1 = sp.diff(second_eqn, y)
    wrt_z1 = sp.diff(second_eqn, z)

    print(wrt_x1 + wrt_y1 + wrt_z1)
    
    term1 = wrt_x1.subs(x, p1)
    term2 = wrt_y1.subs(y, p2)
    term3 = wrt_z1.subs(z, p3)

    equation = term1 + term2 + term3
    print(equation)

    dd = ((t1 + t2 + t3 * term1 + term2 + term3) /
          (sp.sqrt(term1 ** 2 + term2 ** 2 + term3 ** 2)))

    print(float(dd))


while True:

    print("Menu")
    print("1.Along the vector")
    print("2.Toward the point")
    print("3.Normal to the surface")
    print("4.Exit")
    user_choice = int(input("Enter your choice : "))

    eq = sp.sympify(input("Enter the equation: "))
    print("Enter the points:")
    pt1 = int(input("Point 1: "))
    pt2 = int(input("Point 2: "))
    pt3 = int(input("Point 3: "))

    wrt_x = sp.diff(eq, x)
    wrt_y = sp.diff(eq, y)
    wrt_z = sp.diff(eq, z)
    print(wrt_x+wrt_y+wrt_z)
    match user_choice:

        case 1:
            along_the_vector()
        case 2:
            toward_the_point()
        case 3:
            normal_to_surface()
        case 4:
            exit()
