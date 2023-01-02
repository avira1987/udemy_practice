class PinPoint:
    
    def __init__(self, x, y):
        self.x= x
        self.y= y
    def fall_in_rectangel(self, lowleft, upright):
        if lowleft[0]< self.x <upright[0] \
            and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

point1 = PinPoint(10,20)
point1.fall_in_rectangel((5,6),(7,9))