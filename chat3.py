lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())
		
for line in lines:
	s = line.split(' ')
	Time = s[0][ :5]
	name = s[0][5: ]
	print(Time, name)
