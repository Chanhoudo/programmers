def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)):
        if i % m == c-1:
            answer += my_string[i]
    return answer

print(solution("ihrhbakrfpndopljhygc", 4, 2))
print(solution("programmers", 1, 1))

