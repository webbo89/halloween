def random_fact():
	facts = [
		"Banging your head against a wall for one hour burns 150 calories.",
		"Pteronophobia is the fear of being tickled by feathers.",
		"Snakes can help predict earthquakes.",
		"A flock of crows is known as a murder.",
		"The oldest 'your mum' joke was discovered on a 3,500 year old Babylonian tablet."
	]
 	from random import randint
 	index = randint(0, len(facts))
 	print(facts[index])
 