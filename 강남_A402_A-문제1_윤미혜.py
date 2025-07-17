# 계산 함수 선언
def add(x, y):
    return x + y

def substract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    if y == 0:
        print("0 으로 나눌 수 없습니다.")
        exit()
    else:
        return round(x / y, 2)

# 사용자에게 숫자 입력받기
x = input("계산할 첫번째 숫자를 입력하세요 : ")
y = input("계산할 두번째 숫자를 입력하세요 : ")

# 숫자로 변환하기
try:
    x = int(x)
    y = int(y)
except ValueError:
    print("숫자로 입력해주세요.")
    exit()

# 사용 결과 출력
print(f"덧셈 결과 : {add(x,y)}")
print(f"뺄셈 결과 : {substract(x,y)}")
print(f"곱셈 결과 : {multiply(x,y)}")
print(f"나눗셈 결과 : {division(x,y)}")
