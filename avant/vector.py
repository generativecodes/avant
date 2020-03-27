from math import cos, sin, sqrt
from numbers import Number
from random import random

class Vector():
    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return str( "Vector({0.x},{0.y},{0.z})"
                    .format(self))

    def __mul__(self, value):
        if isinstance(value, type(self)):
            return Vector(  value.x * self.x ,
                            value.y * self.y ,
                            value.z * self.z )
        elif isinstance(value, Number):
            return Vector(  self.x * value ,
                            self.y * value ,
                            self.z * value )
        else:
            raise ValueError("Not a Number or Vector.")

    def __rmul__(self, value):
        return self.__mul__(value)

    def __add__(self, value):
        if isinstance(value, type(self)):
            return Vector(  value.x + self.x ,
                            value.y + self.y ,
                            value.z + self.z )
        elif isinstance(value, Number):
            return Vector(  self.x + value ,
                            self.y + value ,
                            self.z + value )
        else:
            raise ValueError("Not a Number or Vector.")

    def __radd__(self, value):
        return self.__add__(value)

    def __sub__(self, value):
        if isinstance(value, type(self)):
            return Vector(  self.x - value.x ,
                            self.y - value.y ,
                            self.z - value.z )
        elif isinstance(value, Number):
            return Vector(  self.x - value ,
                            self.y - value ,
                            self.z - value )
        else:
            raise ValueError("Not a Number or Vector.")

    def __rsub__(self, value):
        if isinstance(value, type(self)):
            return Vector(  value.x - self.x ,
                            value.y - self.y ,
                            value.z - self.z )
        elif isinstance(value, Number):
            return Vector(  value - self.x ,
                            value - self.y ,
                            value - self.z )
        else:
            raise ValueError("Not a Number or Vector.")



    def __truediv__(self, value):
        if isinstance(value, type(self)):
            return Vector(  self.x / value.x ,
                            self.y / value.y ,
                            self.z / value.z )
        elif isinstance(value, Number):
            return Vector(  self.x / value ,
                            self.y / value ,
                            self.z / value )
        else:
            raise ValueError("Not a Number or Vector.")

    def __rtruediv__(self, value):
        if isinstance(value, type(self)):
            return Vector(  value.x / self.x ,
                            value.y / self.y ,
                            value.z / self.z )
        elif isinstance(value, Number):
            return Vector(  value / self.x ,
                            value / self.y ,
                            value / self.z )
        else:
            raise ValueError("Not a Number or Vector.")

    def __mod__(self, value):
        if isinstance(value, type(self)):
            return Vector(  self.x % value.x ,
                            self.y % value.y ,
                            self.z % value.z )
        elif isinstance(value, Number):
            return Vector(  self.x % value ,
                            self.y % value ,
                            self.z % value )
        else:
            raise ValueError("Not a Number or Vector.")

    def __rmod__(self, value):
        if isinstance(value, type(self)):
            return Vector(  value.x % self.x ,
                            value.y % self.y ,
                            value.z % self.z )
        elif isinstance(value, Number):
            return Vector(  value % self.x ,
                            value % self.y ,
                            value % self.z )
        else:
            raise ValueError("Not a Number or Vector.")

    def random_2d():
        return Vector(random(), random(), 0)

    def random_3d():
        return Vector(random(), random(), random())

    @staticmethod
    def from_angle(angle):
        return Vector(cos(angle),sin(angle))

    def rotate(self,angle):
        x = self.x * cos(angle) - self.y * sin(angle)
        y = self.x * sin(angle) + self.y * cos(angle)
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y, self.z)

    def dist(self, vec):
        v =  vec - self
        return mag(v)

    def dot(self, v):
        return self.x*v.x + self.y*v.y + self.z*v.z

    def mag(self):
        return sqrt(self.dot(self))

    def cross(self, v):
        x = self.y*v.z - self.z*v.y
        y = self.z*v.x - self.x*v.z
        z = self.x*v.y - self.y*v.x
        return Vector(x,y,z)






