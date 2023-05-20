class Vector:
	""" Represent a vector in multidimensional Space """
	def __init__(self, n):
		""" Create n-dimensional vector of vector """
		self.__cords = [0] * n
	def __len__(self):
		""" Return the dimention of the vector """
		return len(self.__cords)
	def __getitem__(self, index):
		return self.__cords[index]
	def __setitem__(self, index, value):
		""" Set index cordinate to a given value """
		return self.__cord[index] = value 
	def __add__(self, other):
		""" Return the sum of two vector """
		if len(self) != len(other):
			raise ValueError(' Dimension must be the same' )
		result =  Vector(len(self))
		for j in range(len(self):
			result[j] =  self[j] + other[j]
		return result
	def __eq__(self, other):
		""" Return True if vectors differ from other """
		return self._cords == other._cords
	def __ne__(self, other):
			return not selt == other 
	def __str__(self):
		"""" Produce the string representation of Vector """
		return '<' + str(self._cords)[1: -1] + '>'
	
		
