from queue import Queue
from collections import deque

def printStep(arr, val) :
    print("step%2d " % val, end='')
    print(arr)


# 코드 12.12: 기수 정렬
def radix_sort(A) :
    queues = []
    for i in range(BUCKETS) :
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) : 	            # 자릿수에 따라 큐에 삽입
            queues[(A[i]//factor) % BUCKETS].put(A[i])

        i = 0
        for b in range(BUCKETS) :		    # 버킷에서 꺼내어 list로 합친다.
            while not queues[b].empty() :
                A[i] = queues[b].get()
                i += 1
        factor *= 10					    # 그 다음 자리수로 간다.
        printStep(A, d + 1)			        # 중간 과정 출력용 문장


# 코드 12.13: 기수 정렬 테스트 프로그램  
import random
BUCKETS = 10
DIGITS  = 4

if __name__ == "__main__":
    data = []
    for i in range(10) :
        data.append(random.randint(1,9999))

    radix_sort(data)
    print("Radix: " + str(data))
