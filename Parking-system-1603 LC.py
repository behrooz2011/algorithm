class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.arr = [self.big,self.medium,self.small]
        

    def addCar(self, carType: int) -> bool:
        # print("this is arr:\t",arr)
        if carType == 1:
            self.arr[0] = self.arr[0]-1
            if self.arr[0] >= 0:
                return True
            else:
                return False
    
        if carType == 2:
            self.arr[1]=self.arr[1]-1
            if self.arr[1] >= 0:
                return True
            else:
                return False
        if carType == 3:
            self.arr[2]=self.arr[2]-1
            if self.arr[2] >= 0:
                return True
            else:
                return False