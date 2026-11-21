a = 10 # 변수
PI = 3.141592 # 상수
def add(x): # 함수
	return a * x + 6
class Random:
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def sub(self):
		self.result = self.first + self.second
	def randint(self):
		self.result = self.first / self.second

random = Random(100, 200)



