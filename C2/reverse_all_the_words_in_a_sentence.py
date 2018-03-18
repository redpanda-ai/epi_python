def solution(my_string):
    x = " ".join([word for word in my_string.split(" ")][::-1])
    return x
print(solution("i am batman"))