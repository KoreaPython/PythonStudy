__author__ = 'leftpark'

import math

from class_figure import Circle
from class_figure import Rectangle

# class of Reflecting Object
class Reflect():
    def __init__(self):
        pass

    @staticmethod
    def circle_in_rectangle(circle, rectangle):
        LEFT_SIDE = 1
        # 객체검사: 전달 받은 객체의 클래스 검사
        if not isinstance(circle, Circle) and\
           not isinstance(rectangle, Rectangle):
            return

        side = 0

        if circle.cX() >= rectangle.x and circle.cX() <= rectangle.x + rectangle.ex:
            if circle.x < rectangle.x:
                side = 'left'
            elif (rectangle.x + rectangle.ex - circle.r) <= circle.x:
                side = 'right'

        if circle.cY() >= rectangle.y and circle.cY() <= rectangle.y + rectangle.ey:
            if circle.y < rectangle.y:
                side = 'top'
            elif(rectangle.y + rectangle.ey - circle.r) <= circle.y:
                side = 'bottom'

        print("side = ", side)


        tmp_theta = circle.degree
        print("tmp_theta = ", tmp_theta)

        if (side == 'left' and (90 < tmp_theta and tmp_theta < 180)) or\
           (side == 'right' and (0 < tmp_theta and tmp_theta < 90)):
            circle.degree = 180 - tmp_theta
            print("circle.degree(1) = ",circle.degree)
        elif (side == 'left' and (180 < tmp_theta and tmp_theta < 270)) or\
           (side == 'right' and (270 < tmp_theta and tmp_theta < 360)):
            circle.degree = 540 - tmp_theta
            print("circle.degree(2) = ",circle.degree)
        elif (side == 'top' or side == 'bottom'):
            circle.degree = 360 - tmp_theta
            print("circle.degree(3) = ",circle.degree)
        else:
            print('pass')
            pass