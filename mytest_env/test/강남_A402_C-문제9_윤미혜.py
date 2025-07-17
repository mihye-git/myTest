import threading
import time
import numpy as np

# 짝수 출력 함수
def even(numbers):
    for i in numbers:
        if i % 2 == 0:
            time.sleep(1)
            print(f"짝수 : {i}", end="\n")
    print("Tread_even 작업 종료", end="\n")

# 홀수 출력 함수
def odd(numbers):
    for i in numbers:
        if i % 2 != 0:
            time.sleep(1)
            print(f"홀수 : {i}", end="\n")
    print("Tread_odd 작업 종료", end="\n")

# 1 ~ 10까지 숫자 생성
numbers = np.arange(1, 11)

# Treading
thread_even = threading.Thread(target=even, args=(numbers,))
thread_odd = threading.Thread(target=odd, args=(numbers,))

thread_even.start()
thread_odd.start()

thread_even.join()
thread_odd.join()


