import random
from collections import Counter

# 무작위 숫자 생성
numberList = []

for i in range(0, 30):
    x = random.randint(1, 9)
    numberList.append(x)

# counter 함수 사용
counter = Counter(numberList)

# 내림차순 정렬
sorted_counter = sorted(counter.items(), key=lambda x : x[1], reverse=True)

# 출력
for num, count in sorted_counter:
    print(f"{num} 은 총 {len(numberList)}개 숫자 중 {count}개 생성되었습니다.")
