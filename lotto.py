import random
my_set = set()

def loto():
	while len(my_set) < 7:
		my_set.add(random.randint(1,40))
	print(sorted((my_set)))


loto()
