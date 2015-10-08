__author__ = 'leftpark'

import math

# Helper class for moving a ball
class MovingHelper():
    '''
    오브젝트를 전달받아 다음 위치를 계산해준다.
    '''
    def __init__(self):
        pass


    @classmethod
    def movingToNext(cls, obj):
        '''
        오브젝트의 x좌표와 y좌표의 다음 위치를 계산하고 값을 세팅한다
        :param obj: 이동시킬 오브젝트를 받는다
        :return:
        '''
        # x 좌표의 다음 위치 계산
        obj.x += obj.velocity * math.cos(obj.theta)
        # y 좌표의 다음 위치 계산
        obj.y += obj.velocity * math.sin(obj.theta)