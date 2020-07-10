def rightTriangleCounter(x,y,z): 
	counter = 0 
	side1,side2,side3 = isRightTriangle(x,y,z)  
		counter = counter + 1 
	return counter 

def isRightTriangle(x,y,z): 
	x, y, z = sorted([x, y, z])
	if  x ** 2 + y ** 2 == z ** 2: 
		return x,y,z 