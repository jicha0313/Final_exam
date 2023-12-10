def solution(my_string, target): # 문자열 my_string과 target을 매개변수로 지정
    answer = 0                   # answer값을 0으로 지정
    if target in my_string:      # 만약 문자열 target이 문자열 my_string 안에 있으면
        return 1                 # 1을 반환
    else:                        # 그렇지 않으면
        return answer            # answer 반환
print(solution("open","pe"))     # my_string은 open으로 그리고 target은 pe로 설정