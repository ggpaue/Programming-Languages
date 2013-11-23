class Complex: 
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag
	
	# real part
	def realpart(self):
		return self.real

	# imaginary part
	def imagpart(self): 
		return self.imag

	# Addition
	def add(self, num):
		real = self.real + num.real
		imag = self.imag + num.imag
		return Complex(real, imag)

	# Subtraction
	def subtraction(self, num):
		real = self.real - num.real
		imag = self.imag - num.imag
		return Complex(real, imag)

	# Multiplication
	def multiple(self, num):
		real = self.real * num.real - self.imag * num.imag
		imag = self.real * num.imag + self.imag * num.real
		return Complex(real, imag)

	# Division
	def divide(self, num):
		denominator = num.real ** 2 + num.imag ** 2
		real = self.real * num.real + self.imag * num.imag
		imag = self.imag * num.real - self.real * num.imag
		return Complex((real / denominator), (imag / denominator))

	# Display
	def __str__(self):
		if self.real == 0:
			return str(self.imag) + "j"
		elif self.imag == 0:
			return str(self.real)
		elif self.imag < 0:
			return str(self.real) + " " + str(self.imag) + "j"
		else:
			return str(self.real) + " " + "+" + " " + str(self.imag) + "j"


# Test
a = 2.0
b = 3.0
c = 5.0
d = 7.0

x = Complex(a,b)	   # take variables as parameters
y = Complex(c,d)
z = Complex(a + b, c + d)  # take expressions as parameters
	
print("Real part of x: ", x.realpart())
print("Imaginary part of x: ", x.imagpart())
print("Real part of y: ", y.realpart())
print("Imaginary part of y: ", y.imagpart())
print("Real part of z: ", z.realpart())
print("Imaginary part of z: ", z.imagpart())
	
print("x = ", x)
print("y = ", y)
print("x + y = ", x.add(y))
print("x - y = ", x.subtraction(y))
print("x * y = ", x.multiple(y))
print("x / y = ", x.divide(y))	
print("x + z = ", x.add(z))
print("z * y = ", z.multiple(y))



	
	
	
		
