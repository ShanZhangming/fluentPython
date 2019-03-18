
def make_averger():
	count = 0
	total = 0
	def averger(new_value):
		nonlocal count,total
		count += 1
		total += new_value
		return total/count
	return averger

avg = make_averger()
print(avg(10))
print(avg(11))