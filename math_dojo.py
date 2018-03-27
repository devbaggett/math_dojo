# assignment title
print "\n----------Assignment: MathDojo----------\n"

# create class: "MathDojo"
class MathDojo(object):
	# this method to run every time a new object is instantiated
	def __init__(self):
		self.total = 0
	
	# method that adds any amount of numbers when invoked
	def add(self, *nums):
		# iterates through *nums to get numbers from lists and tuples if necessary
		for num in nums:
			if type(num) == list:
				self.total += sum(num)
			else:
				self.total += num
		return self

	def subtract(self, *nums):
		# iterates through *nums to get numbers from lists and tuples if necessary
		for num in nums:
			if type(num) == list:
				self.total -= sum(num)
			else:
				self.total -= num
		return self

	# displays result of MathDojo
	def result(self):
		print "Result: {}".format(self.total)
		return self
		
# create MathDojo instances
md = MathDojo()
md2 = MathDojo()

print "\n-----Answer 1-----"
# result1
md.add(2).add(2,5).subtract(3,2).result()

print "\n-----Answer 2-----"
# result2
md2.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

# end separator
print ""