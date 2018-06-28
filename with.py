a = []
with open('C:/Users/Also_Lenovo/Desktop/reviews.txt', 'r') as txt:
	for t in txt:
		a.append(t.strip())
		#print(t)
		print(a)