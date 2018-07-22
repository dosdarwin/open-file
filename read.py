a = []
count = 0
with open('C:/Users/Also_Lenovo/Desktop/reviews.txt', 'r') as txt:
	for t in txt:
		a.append(t.strip())
		#count += 1
		# if count % 1000 == 0:
		# 	print(count)
			

wc = {}
for words in a:
	words = words.split()
	# print(words)
	for word in words:
		if word in wc:e
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

while True:
	check = input('type the word you want to find:')
	if check == 'q':
		print('Thank you for using')
		break
	if check in wc:
		print(check,':',wc[check])
	else:
		print('cannot find it')

#print(wc)