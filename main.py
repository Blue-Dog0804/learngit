from abc import ABCMeta, abstractmethod

class Student(metaclass=ABCMeta):
	def __init__(self, name, age):
		self.name = name
		self.age = age
    @abstractmethod
	def fun(self):
		pass
class Me(Student):
    def __init__(self, name, age, gender):
        Student.__init__(self, name, age)
        self.gender = gender
    def fun(self):
        print('method done')
def test():
	print('hello world')

if __name__ = '__main__':
	test()
