from ArrayStack import ArrayStack


def checkBrackets(statement):
    stack = ArrayStack(100)
    line_idx = 1  # 현재 라인 번호
    string_idx = 0  # 현재 라인에서의 문자 위치

    for ch in statement:
        if ch == '\n':
            line_idx += 1
            string_idx = 0
        else:
            string_idx += 1

        if ch == '{' or ch == '[' or ch == '(':
            stack.push((ch, line_idx, string_idx))

        elif ch == '}' or ch == ']' or ch == ')':
            if stack.isEmpty():
                print(
                    f"조건 2(같은 타입의 괄호에서 왼쪽 괄호가 오른쪽 괄호보다 먼저 나와야 한다)를 위배합니다. (라인 {line_idx}, 문자 {string_idx})")
                return

            left, left_line, left_string = stack.pop()
            if (ch == '}' and left != '{') or \
               (ch == ']' and left != '[') or \
               (ch == ')' and left != '('):
                print(
                    f"조건 3(서로 다른 타입의 괄호 쌍이 서로를 교차하면 안 된다)를 위배합니다. (라인 {left_line}, 문자 {left_string})")
                return

    if not stack.isEmpty():
        left, left_line, left_string = stack.pop()
        print(
            f"조건 1(왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야한다)를 위배합니다. (라인 {left_line}, 문자 {left_string})")


def check_file(fileName):
    with open(fileName, 'r') as file:
        python_code = file.read()
        checkBrackets(python_code)


def main():
    python_file = input("파이썬 소스 파일의 이름을 입력하세요: ")
    check_file(python_file)
