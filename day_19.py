### 1. 随机整数生成类
# 可以指定一批生成的个数，可以指定数值的范围，可以调整每批生成数字的个数
import random

class RandomInt:
    def __init__(self, count: int, start: int, end: int):
        self._count = count
        self._start = start
        self._end = end
        self._nums = []

    def buildnums(self):
        for c in range(self._count):
            self._nums.append(random.randint(self._start, self._end))
        return self._nums

    def point(self):
        for i in range(0, len(self._nums), 2):
            yield (self._nums[i], self._nums[i+1])


# r = RandomInt(20, 1, 10)
# print(r.buildnums())





# 普通类实现
class RandomGen:
    def __init__(self,count,start,end):
        self.count = count
        self.start = start
        self.end = end

    def generate(self):
        return [random.randint(self.start,self.end) for i in range(self.count)]

# print(RandomGen(10,1,5).generate())


# 作为工具类实现

class RandomGen2:
    @classmethod
    def generate(cls,start=1,end=6,count=10):
        return [random.randint(start,end) for _ in range(count)]

# print(RandomGen2.generate())



# 生成器实现
class RandomGen3:
    def __init__(self,start,end,count):
        self.start = start
        self.end = end
        self.count = count
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield random.randint(self.start,self.end)

    def generate(self,count=0):
        count = self.count if count <= 0 else count
        return [next(self._gen) for _ in range(count)]

# print(RandomGen3(1,5,10).generate())

# class RandomGen:





# 生成器的另一种实现方式
class RandomGen4:
    def __init__(self,start=1,end=10,patch=10):
        self.start = start
        self.end = end
        self._patch = patch
        self._gen = self._generate()

    def _generate(self):
        yield [random.randint(self.start,self.end) for _ in range(self._patch)]

    def generate(self,patch=0):
        if patch > 0:
            self._patch = patch
        return next(self._gen)


# print(RandomGen4().generate(5))


# @proparty
class RandomGen5:
    def __init__(self,start=1,end=5,patch=10):
        self.start = start
        self.end = end
        self._patch = patch
        self._gen = self._generate()

    def _generate(self):
        yield [random.randint(self.start,self.end) for _ in range(self._patch)]

    def geterate(self,patch = 0):
        if patch > 0:
            self._patch = patch
        return next(self._gen)

    @property
    def patch(self):
        return self._patch

    @patch.setter
    def patch(self,value):
        self._patch = value


# r = RandomGen5()
# print(RandomGen5().geterate(5))
# print(r.patch)
# r.patch = 5
# print(r.geterate())










### 2、打印坐标
# 使用上题中的类，随机生成20个数，两两配对形成二维坐标，把坐标组织起来，并打印输出

# r = RandomInt(20, 1, 10)
# for i in r.point():
#     print(i)

class Point:
    def __init__(self,lst):
        self.lst = lst

    def point(self):
        nums = self.lst
        for i in range(0, len(nums), 2):
            yield (nums[i], nums[i+1])


# r = RandomInt(20, 1, 10)
# print(r.buildnums())
# lst = r.buildnums()
# p = Point(lst)
# print(next(p.point()))




class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

# poins = [Point(x,y) for x,y in zip(RandomGen5().geterate(10),RandomGen5().geterate(10))]
# for p in poins:
#     print(p.x,p.y)









### 3、车牌信息
# 记录车的品牌mark、颜色color、价格price、速度speed等特征，并实现增加车辆的信息、显示全部车辆信息的功能
class Car:
    def __init__(self, mark, color, price, speed):
        self.mark = mark
        self.color = color
        self.price = price
        self.speed = speed


class CarInfo:
    def __init__(self):
        self.carinfo = []

    def addcar(self, car):
        self.carinfo.append(car)

    def getcarinfo(self):
        return self.carinfo


# carinfo = CarInfo()
# newcar1 = Car('Audi','black','30W','200km/h')
# newcar2 = Car('bmw','black','30W','200km/h')
# # print(newcar.__dict__)
# carinfo.addcar(newcar1)
# carinfo.addcar(newcar2)
# # print(carinfo.__dict__)
# infolist = carinfo.getcarinfo()
# print(infolist)
# for info in infolist:
#     print(info.__dict__)












### 4、实现温度的处理
# 实现华氏温度和摄氏温度的转换。
# C = 5*(F-32) / 9
# F = 9*C /5 + 32
# 完成以上转后后，增加与开氏温度的转换， K = C+ 273.15

class Temperature:
    _icepoint = 32
    _kel = 273.15
    # def __init__(self, unit='℃'):
    #     self._icepoint = 32
    #     self._kel = 273.15

    @classmethod
    def celsius2fahrenheit(self, celsius):
        return '{}{}'.format(int(9 * celsius / 5 + self._icepoint),"℉")

    @classmethod
    def celsius2kelvin(self, celsius):
        return '{}{}'.format(int(celsius + self._kel),'K')

    @classmethod
    def fahrenheit2celsius(self, fahrenheit):
        return '{}{}'.format(int(5 * (fahrenheit - self._icepoint) / 9),'℃')

    @classmethod
    def fahrenheit2kelvin(self, fahrenheit):
        return '{}{}'.format(int((fahrenheit + 459.67) / 9 * 5),'K')

    @classmethod
    def kelvin2celsius(self,kelvin):
        return '{}{}'.format(int(kelvin - self._kel),'℃')

    @classmethod
    def kelvin2fahrenheit(self,kelvin):
        return '{}{}'.format(int(kelvin * 1.8 - 459.67),'℉')




# temperature = Temperature()
# print(Temperature.celsius2fahrenheit(30))

# print(temperature.celsius2kelvin(30))
# print(temperature.fahrenheit2celsius(86))
# print(temperature.fahrenheit2kelvin(120))
# print(temperature.kelvin2celsius(545))
# print(temperature.kelvin2fahrenheit(545))








class Temperature:
    _icepoint = 32
    _kel = 273.15
    def __init__(self,t,unit='c'):
        self._k = None
        self._f = None
        self._c = None

        if unit == 'k':
            self._k = t
            self._c = self.k2c(t)
        elif unit == 'f':
            self._f = t
            self._c = self.f2c(t)
        else:
            self._c = t

    @property
    def c(self): # 摄氏度
        return self._c

    @property
    def f(self): # 华氏温度
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @property
    def k(self): # 开氏温度
        if self._k is None:
            self._k = self.c2k(self._c)
        return self._k

    # 温度转换
    @classmethod
    def c2f(cls,c):
        return 9*c/5 + 32

    @classmethod
    def c2k(cls,c):
        return c + cls._kel

    @classmethod
    def f2c(cls,f):
        return 5*(f-32)/9

    @classmethod
    def f2k(cls,f):
        return cls.c2k(cls.f2c(f))


    @classmethod
    def k2c(cls,k):
        return k - cls._kel

    @classmethod
    def k2f(cls,k):
        return cls.c2f(cls.k2c(k))



# print(Temperature.c2f(30))
# print(Temperature.c2k(30))
# print(Temperature.f2c(86))
# print(Temperature.f2k(86))
# t = Temperature(30)
# print(t.c,t.k,t.f)
# t = Temperature(303,'k')
# print(t.c,t.f,t.k)










### 5、 模拟购物车购物
class ShoppingCar:
    def __init__(self,color,wheel):
        self._color = color
        self._wheel = wheel
        self.volume = []
        # self.lst = [1,2,3]

    def add_items(self,items):
        self.volume.append(items)

    def get_info(self):
        return shc.volume




class Goods:
    def __init__(self,mark,color,func):
        self._mark = mark
        self._color = color
        self._func = func

# shc = ShoppingCar('black','4')
# apple = Goods('hfs','red','eat')
# computer = Goods('asus','white','study')
# shc.add_items(apple)
# shc.add_items(computer)
# print(shc.get_info())

# for info in shc.get_info():
#     print(info.__dict__)