# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


#
#      A2 (5.15)_______________A3 (15.15)
#              /             /
#             /             /
#            /             /
#  A1 (0.0) /_____________/A4 (10.0)

A1, A2, A3, A4 = (0, 0), (5, 15), (15, 15), (10, 0)
if A4[0] - A1[0] == A3[0] - A2[0] and A4[1] - A1[1] == A3[1] - A2[1] and A2[1] - A1[1] == A3[1] - A4[1] and A2[0] - A1[
    0] == A3[0] - A4[0]:
    print('Good')
else:
    print('Bad')
