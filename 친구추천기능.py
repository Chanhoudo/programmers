# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M = input().split(" ")
eq_f = 0
login_h = input().split(" ")
f_f = []
l_f = []
for i in range(int(M)):
	f_f.append(input().split(" "))

	
for i in range(round(int(M)/2)):
	for j in range(round(int(M)/2), int(M)):
		if f_f[i][1] == f_f[j][1]:
			eq_f = eq_f + 1
			
l_f.append(f_f[0][0])
l_f.append(f_f[int(M)-1][0])
l_f = sorted(l_f)

for p in l_f:
	print(f'{p}', end =" ")
print()
print(eq_f)