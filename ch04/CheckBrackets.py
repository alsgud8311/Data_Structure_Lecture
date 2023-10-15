from ArrayStack import ArrayStack  # 기존 자료구조에 있는 ArrayStack 모듈 import
# 괄호 일치 검사 함수


def checkBrackets(statement):
    stack = ArrayStack(100)  # 스택 생성, 사이즈는 약 100정도 설정
    line_idx = 1  # 현재 라인 번호를 초기화
    string_idx = 0  # 현재 라인에서의 문자 위치를 초기화(문자열은 0부터 시작)

    for ch in statement:
        if ch == '\n':
            line_idx += 1  # 줄바꿈 문자를 만나면 라인 번호를 증가시키기
            string_idx = 0  # 문자 위치를 다시 0으로 초기화하여 해당 라인의 처음부터 검사
        else:
            string_idx += 1  # 그 외의 문자일 경우 문자 위치를 옆으로 하나씩 옮겨가며 검사

        if ch == '{' or ch == '[' or ch == '(':
            # 열린 괄호의 경우 문제 없기 때문에 바로 스택에 push
            stack.push((ch, line_idx, string_idx))

        elif ch == '}' or ch == ']' or ch == ')':
            if stack.isEmpty():
                # 닫는 괄호의 경우 스택이 비어 있는데 닫힌 괄호가 나올 경우 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다는 조건을 위배하므로 해당 오류 메세지와 인덱스를 반환
                print(
                    f"조건 2(같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다)를 위배합니다. (라인 {line_idx}, 문자 {string_idx})")
                return

            left, left_line, left_string = stack.pop()
            # 여는 괄호가 있을 경우 스택에서 pop해서 왼쪽의 여는 괄호를 찾기
            if (ch == '}' and left != '{') or \
               (ch == ']' and left != '[') or \
               (ch == ')' and left != '('):
                # 해당 조건은 서로 괄호가 맞지 않는 경우이므로 조건 3에 위반하는 조건들
                # 해당 조건에 위배한다면 오류 메세지와 함께 인덱스 반환
                print(
                    f"조건 3(서로 다른 타입의 괄호 쌍이 서로를 교차하면 안 된다)를 위배합니다. (라인 {left_line}, 문자 {left_string})")
                return

    if not stack.isEmpty():
        # 해당 for문을 다 빠져나왔음에도 불구하고 서로 개수가 맞지 않으면 남는 괄호가 생길 수 있음
        # 이 경우 for문을 통해
        print(
            f"조건 1(왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 한다)를 위배합니다. (라인 {left_line}, 문자 {left_string})")
    # 모든 조건 충족 시 0 반환
    else:
        print("0")

# 파일에서 괄호 일치 검사 함수 호출


def check_file(fileName):
    with open(fileName, 'r') as file:
        python_code = file.read()
        checkBrackets(python_code)

# 메인 함수


def main():
    python_file = input("파이썬 소스 파일의 이름을 입력하세요: ")  # 사용자로부터 파일 이름을 입력받음
    check_file(python_file)  # 입력된 파일에 대해 괄호 일치 검사 함수를 호출


if __name__ == "__main__":
    main()  # 스크립트가 직접 실행될 때 메인 함수를 호출합니다.
