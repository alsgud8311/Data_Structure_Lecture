
def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)

# 코드 12.1: 셸 정렬에 사용되는 삽입정렬 
# gap 만큼 떨어진 요소들을 삽입 정렬. 정렬의 범위는 first에서 last 
def sortGapInsertion(A, first, last, gap) :
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :
            A[j + gap] = A[j]
            j = j - gap
        A[j + gap] = key


# 코드 12.2: 셸 정렬 알고리즘def shell_sort(A) :
    n = len(A)
    gap = n//2
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1	# gap이 짝수이면 1을 더함 
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap);
        print('     Gap=', gap, A)
        gap = gap//2
        #printStep(A, count)		    # 중간 과정 출력용 문장 


if __name__ == "__main__":
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    print("Original  :", data)
    shell_sort(data)
    print("Shell     :", data)
