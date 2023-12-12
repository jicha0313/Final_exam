def solution(numbers): # numbers를 변수로 사용하는 함수
    answer = '' # 공백으로 초기화
    
    numbers = list(map(str, numbers)) # 숫자 리스트를 문자열 리스트로
    numbers.sort(reverse=True) # 내림차순으로 정렬
    
    for i in numbers: 
        answer += i # 정렬된 리스트를 answer에 순서대로 더해줌
    
    return answer
print(solution("4 40 49"))