class Polygon(object):
	def CalcArea():
		pass
	
class Rectangle(Polygon):
	def __init__(self,length,width):
		self.__length=length
		self.__width=width
		pass
		
	def CalcArea(self):
		
		area=self.__length*self.__width
		print(area)

class Triangle(Polygon):
    def __init__(self,length,height):
    	self.__length=length
    	self.__height=height
    	pass

    def CalcArea(self):
    	area=0.5*self.__length*self.__height
    	print(area)
class Circle(Polygon):
    		
    def __init__(self,radius):
    	self.radius=radius

    def CalcArea(self):
    	from math import pi
    	area=pi * self.radius*self.radius
    	print(area)
    			
    			    	
rect=Rectangle(10,30)
rect.length=10
rect.width=30
rect.CalcArea()
tri=Triangle(20,10)
tri.length=20
tri.height=10
tri.CalcArea()
circle=Circle(7)
circle.radius=7
circle.CalcArea()
