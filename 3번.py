def solution(age): # age를 변수로 사용하는 함수
    answer = '' # 공백으로 초기화
    alphabet = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f',
            '6':'g', '7':'h', '8':'i', '9':'j'} # dictionary로 각 알파벳의 숫자를 지정
    
    for i in str(age): # 숫자를 문자로 변환한 그 요소만큼 반복
        answer+=(alphabet[i]) # 그 요소를 key값으로 하는 숫자를 answer에 추가
    return answer # answer 반환
print(solution("857")) # 문제에 주어진 857을 입력 및 solution을 호출해서 출력