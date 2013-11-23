# Greatest common divisor of two numbers
def gcd(a, b):
	i = abs(a)
	j = abs(b)
	result = 1
	temp = 1

	while temp <= i and temp <= j:
		if a % temp == 0 and b % temp == 0:
			result = temp
		temp += 1
	return result


class Rational:
	def __init__(self, numerator, denominator):
		divisor = gcd(numerator, denominator)
		flag = 1
		if denominator < 0:
			flag = -1		
		self.numerator = flag * (int)(numerator / divisor)
		self.denominator = (int)(denominator / divisor)

	# get numerator
	def numer(self):
		return self.numerator

	# get denominator
	def denom(self):
		return self.denominator

	# Addition
	def add(self, num):
		numer = self.numerator * num.denom() + self.denominator * num.numer()
		denom = self.denominator * num.denom()
		return Rational(numer, denom)

	# Subtraction
	def sub(self, num):
		numer = self.numerator * num.denom() - self.denominator * num.numer()
		denom = self.denominator * num.denom()
		return Rational(numer, denom)

	# Multiplication
	def mul(self, num):
		numer = self.numerator * num.numer()
		denom = self.denominator * num.denom()
		return Rational(numer, denom)

	# Division
	def div(self, num):
		numer = self.numerator * num.denom()
		denom = self.denominator * num.numer()
		return Rational(numer, denom)

	# Equality Testing
	def equal(self, num):
		result = self.sub(num).numer()
		return result == 0

	# Display
	def __str__(self):
		if self.denominator == 1:
			return str(self.numerator)
		elif self.numerator == 0:
			return str(self.numerator)
		else:
			return str(self.numerator) + " / " + str(self.denominator)

# Test
x = Rational(1, 2)
y = Rational(2, 4)
z = Rational(5, 6)

print("x = ", x)
print("y = ", y)
print("z = ", z)


print("Numerator of x: ", x.numer())
print("Denominator of x: ", x.denom())
print("Numerator of y: ", y.numer())
print("Denominator of y: ", y.denom())
print("Numerator of z: ", z.numer())
print("Denominator of z: ", z.denom())

print("x + y = ", x.add(y))
print("x - y = ", x.sub(y))
print("y * z = ", y.mul(z))
print("x / z = ", x.div(z))
print("x equals y = ", x.equal(y))
print("x equals z = ", x.equal(y))


		
