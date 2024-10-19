# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, M, K, D = input().split(" ")
p_list = input().split(" ")
n_n_l = []
y_n = 0
for i in range(int(M)):
	n_n_l.append(input().split(" "))
	
for i in range(int(M)):
	for j in range(len(p_list)):
		if (n_n_l[i][0] == p_list[j] or n_n_l[i][1] == p_list[j]) and int(n_n_l[i][2]) <= int(D):
			p_list.append(n_n_l[i][0])
			p_list.append(n_n_l[i][1])

p_list = set(p_list)

print(len(p_list))