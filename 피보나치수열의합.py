# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
pibo = []
#def p_bo(n):
#	if n <= 2:
#		return 1
#	else:		
#		return p_bo(n-1) + p_bo(n-2)

start, end = input().split(" ")
answer = 0
for i in range(int(end)):
	if i <= 1:
		pibo.append(1)
	else:
		pibo.append(pibo[i-1] + pibo[i-2])

for i in range(int(start), int(end) + 1):
	answer = round((answer + pibo[i-1]) % (pow(10, 9) + 7))

print(answer)