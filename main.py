# import sympy as sp
# import math
#
# # Defining Symbols
# x, y, z = sp.symbols("x y z")
# i, j, k = sp.symbols("i j k")
#
# # Functions for directional derivatives
# def along_the_vector(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3):
#     print("Enter the vectors field:")
#     vec1 = int(input("i = "))
#     vec2 = int(input("j = "))
#     vec3 = int(input("k = "))
#
#     dd = ((wrt_x * vec1 + wrt_y * vec2 + wrt_z * vec3) /
#           (sp.sqrt((vec1 ** 2 + vec2 ** 2 + vec3 ** 2))))
#
#     print("Directional Derivative along the vector:", sp.simplify(dd))
#
# def toward_the_point(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3):
#     print("Enter the points toward which you want to find D.D:")
#     toward_pt1 = int(input("Point 1: "))
#     toward_pt2 = int(input("Point 2: "))
#     toward_pt3 = int(input("Point 3: "))
#
#     a_b_bar1 = toward_pt1 - pt1
#     a_b_bar2 = toward_pt2 - pt2
#     a_b_bar3 = toward_pt3 - pt3
#
#     dd = (wrt_x * a_b_bar1 + wrt_y * a_b_bar2 + wrt_z * a_b_bar3) / (
#         sp.sqrt((a_b_bar1 ** 2 + a_b_bar2 ** 2 + a_b_bar3 ** 2)))
#
#     print("Directional Derivative toward the point:", sp.simplify(dd))
#
# def normal_to_surface(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3):
#     eq1 = input("Enter the second equation: ")
#     p1 = int(input("Point 1: "))
#     p2 = int(input("Point 2: "))
#     p3 = int(input("Point 3: "))
#
#     wrt_x1 = sp.diff(eq1, x)
#     wrt_y1 = sp.diff(eq1, y)
#     wrt_z1 = sp.diff(eq1, z)
#
#     en1 = wrt_x1.subs(x, p1)
#     en2 = wrt_y1.subs(y, p2)
#     en3 = wrt_z1.subs(z, p3)
#
#     term = wrt_x.subs(x, pt1) + wrt_y.subs(y, pt2) + wrt_z.subs(z, pt3)
#     term1 = en1 + en2 + en3
#
#     dd = term * (term1 / (math.sqrt(en1 ** 2 + en2 ** 2 + en3 ** 2)))
#
#     print("Directional Derivative normal to the surface:", sp.simplify(dd))
#
#
# while True:
#     print("Menu")
#     print("1. Along the vector")
#     print("2. Toward the point")
#     print("3. Normal to the surface")
#     print("4. Exit")
#     user_choice = int(input("Enter your choice : "))
#
#     eq = input("Enter the equation: ")
#     print("Enter the points:")
#     pt1 = int(input("Point 1: "))
#     pt2 = int(input("Point 2: "))
#     pt3 = int(input("Point 3: "))
#
#     wrt_x = sp.diff(eq, x)
#     wrt_y = sp.diff(eq, y)
#     wrt_z = sp.diff(eq, z)
#
#     if user_choice == 1:
#         along_the_vector(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3)
#     elif user_choice == 2:
#         toward_the_point(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3)
#     elif user_choice == 3:
#         normal_to_surface(wrt_x, wrt_y, wrt_z, pt1, pt2, pt3)
#     elif user_choice == 4:
#         break
#     else:
#         print("Invalid choice. Please try again.")

