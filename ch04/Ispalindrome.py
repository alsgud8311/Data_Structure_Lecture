from ArrayStack import ArrayStack


def isPalindrome(text):
    stack = ArrayStack(100)  # Stack 생성
    eng = 'qwertyuiopasdfghjklzxcvbnm'  # 영어만 골라내기 위한 변수
    text_lowerCase = text.lower()  # 모두 소문자로 바꾸기
    text_filtered = ""  # Stack에 있는 문자과 비교할 필터링된 문자열

    for i in text_lowerCase:  # 소문자 필터링된 문자열을 돌면서 영어만 골라내기
        if i in eng:  # a~z 중에 해당 문자가 있는지 확인
            stack.push(i)  # 조건에 부합한다면 stack에 push
            text_filtered += i  # 비교할 문자열에도 넣어주기

    j = 0  # 반복문을 돌 때 인덱스를 하나씩 옮기며 확인해야 하기 때문에 따로 지정
    while not stack.isEmpty():  # stack에 있는 문자가 없을 때까지 반복
        if text_filtered[j] == stack.pop():  # stack에서 꺼낸 문자가 해당 문자열과 같을 경우
            pass  # 반복문을 계속해서 돌리도록 만듦
        else:  # 같지 않을 경우 팰린드롭이 아니므로
            return print('Not Palindrome')  # 바로 리턴하여 반복문 빠져나가기
        j += 1  # j의 인덱스 하나씩 옆으로 옮기기
    return print('Palindrome')  # 모든 조건에 부합하여 stack이 비었을 경우 팰린드롬이 맞으므로 맞다고 리턴


def main():  # 프로그램 실행
    check_text = input("팰린드롬을 확인할 문자를 알려주세요: ")  # 사용자로부터 문자열 받기
    isPalindrome(check_text)


main()
