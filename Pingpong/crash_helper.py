__author__ = 'leftpark'

import math

from class_figure import Line
from class_figure import Circle
from class_figure import Rectangle

# class of Checking Crash
class Crash():
    '''
    객체들이 충돌했는지 확인함
    '''
    def __init__(self):
        pass

    @staticmethod
    def circle_circle():
        pass


    @staticmethod
    def circle_line():
        pass


    @staticmethod
    def circle_out_rectangle(circle, rectangle):
        # 객체검사 : 전달받은 객체의 클래스 검사
        if not isinstance(circle, Circle) and\
           not isinstance(rectangle, Rectangle):
            return

        # 충돌검사 : 객체들이 서로 부딪쳤는지 알아본다
        if circle.cX() < rectangle.x: # 가장 가까운 수직선은 왼쪽 수직선이다
            close_x = rectangle.x # 가장 가까이 있는 x좌표를 찾는다
        elif circle.cX() > rectangle.x + rectangle.ex: # 가장 가꾸은 수직선은 오른쪽 수직선이다
            close_x = rectangle.x + rectangle.ex
        else:
            close_x = circle.cX()

        print("X : ", circle.cX(), close_x)

        if circle.cY() < rectangle.y:
            close_y = rectangle.y # 가장 가까이 있는 y좌표를 찾는다
        elif circle.cY() > rectangle.y + rectangle.ey:
            close_y = rectangle.y + rectangle.ey
        else:
            close_y = circle.cY()

        z = (abs(circle.cX() - close_x) ** 2) + (abs(circle.cY() - close_y) ** 2)
        z = math.sqrt(z)
        print("Y : ",circle.cY(), close_y)
        print("x^2 = ", (abs(circle.cX() - close_x) ** 2))
        print("y^2 = ", (abs(circle.cY() - close_y) ** 2))
        print("z : ", z)

        if z < circle.r/2:
            print("Crash")
        else:
            print("Not Crash")

    @staticmethod
    def circle_in_rectangle(circle, rectangle):
        # 객체검사 : 전달받은 객체의 클래스 검사
        if not isinstance(circle, Circle) and\
           not isinstance(rectangle, Rectangle):
            return

        # 충돌검사 : 객체들이 서로 부딪쳤는지 알아본다
        # 원점의 x 좌표가 사각형의 시작 x 좌표보다 크거나 같고
        # 원점의 x 좌표가 사각형의 끝 x 좌표보다 작거나 같으면
        if circle.cX() >= rectangle.x and circle.cX() <= rectangle.x + rectangle.ex:
            if circle.x < rectangle.x or (rectangle.x + rectangle.ex - circle.r) <= circle.x:
                print("Crash X")
                circle.theta += (math.pi/180)*180
                return True

            print("Not Crash X")

        if circle.cY() >= rectangle.y and circle.cY() <= rectangle.y + rectangle.ey:
            if circle.y < rectangle.y or (rectangle.y + rectangle.ey - circle.r) <= circle.y:
                print("Crash Y")
                return True

            print("Not Crash Y")

        return False


    @staticmethod
    def circle_line(x, y):
        pass