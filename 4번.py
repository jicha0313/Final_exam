import math # math함수를 사용하기 위해 library를 불러옴

def solution(r1, r2): # r1과 r2를 변수로 지정
    answer = 0 # answer을 0으로 초기화
    for x in range(1, r2 + 1):  # 범위함수인 range를 이용해 1부터 시작해서 r2에서 끝나는 범위를 지정
        big_y = math.floor(math.sqrt(r2**2 - x**2)) # 원의 공식을 이용해 y좌표를 구하고 정수인 값만 구할 것이기 때문에 math.floor를 통해 내림
        small_y = 0 if x >= r1 else math.ceil(math.sqrt(abs(r1**2 - x**2))) # 마찬가지로 원의 공식을 이용해 y좌표를 구하고 정수만 구할 것이기 때문에 math.ceil을 통해 올림
        answer += big_y - small_y + 1 # big_y에서 small_y를 빼고 1을 더해줌
    
    return answer * 4 # answer*4 반환
print(solution(3, 4)) # r1에 3, r2에 4을 입력 및 solution을 호출해서 출력