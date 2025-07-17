import random

# 복권번호 생성
x = random.randint(10, 30)

# 사용자에게 복권 번호 받기
userInput = input("복권 번호를 입력하세요. (두 자리 숫자) : ") 

# 두 자리 숫자가 아니면 종료
if len(userInput) != 2:
    print("두자리 숫자만 입력 가능합니다.")
    exit()

# 사용자가 입력한 데이터 문자 → 숫자 변환
try:
    userInput = int(userInput)
except ValueError:
    print("숫자로 입력해주세요.")
    exit()

# 사용자 데이터와 복권 번호 리스트에 담기
userInputList = []
xList = []

for i in str(userInput):
    userInputList.append(i)

for i in str(x):
    xList.append(i)


# 상금 출력 (순서 무관)
if all(num in userInputList for num in xList):
    print("100만원 당첨!")
elif any(num in userInputList for num in xList):
    print("50만원 당첨!")
else :
    print("꽝!")

