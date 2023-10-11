# 코드 12.10: 이중 피벗 퀵 정렬
def dp_quick_sort(A, low, high) :
    if low < high :
        lp, rp = partitionDP(A, low, high)  # 좌우 피벗의 인덱스를 반환받음
        dp_quick_sort(A, low, lp-1)         # low ~ lp-1 정렬
        dp_quick_sort(A, lp+1, rp-1)        # lp+1 ~ rp-1 정렬
        dp_quick_sort(A, rp+1, high)        # rp+1 ~ high 정렬


# 코드 12.11: 이중피벗 퀵 정렬을 위한 분할 함수
def partitionDP(A, low, high) :
    if A[low] > A[high]:            # 오른쪽 피벗은 왼쪽보다 작지 않아야 함.
        A[low], A[high] = A[high], A[low]

    j = low + 1                     # lp보다 작은 최대 인덱스
    g = high - 1                    # rp보다 큰 최소 인덱스
    k = low + 1                     # low+1부터 하나씩 증가
    lpVal = A[low]                  # 왼쪽 피벗 값
    rpVal = A[high]                 # 오른쪽 피벗 값
    while (k <= g) :
        if (A[k] < lpVal) :         # A[k]가 왼쪽 피벗보다 작으면
            A[k], A[j] = A[j], A[k] # 교환
            j += 1 

        elif (A[k] >= rpVal) :      # 오른쪽 피벗보다 크거나 같으면
            while (A[g] > rpVal  and  k < g) :  # g의 위치를 찾은 후 
               g -= 1
            A[k], A[g] = A[g], A[k] # A[k] <-> A[g]
            g -= 1

            if (A[k] < lpVal) :     # 변경된 A[k]가 왼쪽 피벗보다 작으면
                A[k], A[j] = A[j], A[k]     # 다시 교환
                j += 1 
        k += 1 

    j -= 1 
    g += 1 
    A[low], A[j] = A[j], A[low]     # 피벗을 제 위치로: j:왼쪽피벗
    A[high], A[g] = A[g], A[high]   # 피벗을 제 위치로: g:왼쪽피벗
  
    return j, g     # 왼쪽과 오른쪽 피벗의 인덱스

if __name__ == "__main__":
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    print("Original  :", data)
    dp_quick_sort(data, 0, len(data)-1) 
    print("DPQuick   :", data)

