sorted = [0]*100

# 코드 12.6: 병합 정렬
def merge_sort(A, left, right) :
	if left<right :
		mid = (left + right) // 2		# 리스트의 균등 분할
		merge_sort(A, left, mid)		# 부분 리스트 정렬
		merge_sort(A, mid + 1, right)	# 부분 리스트 정렬
		merge(A, left, mid, right)	    # 병합


# 코드 12.7: 병합 정렬을 위한 merge() 함수
def merge(A, left, mid, right) :
    global sorted
    k = left			# k는 정렬될 리스트에 대한 인덱스
    i = left
    j = mid + 1
    while i<=mid and j<=right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
            #i += 1
            #k += 1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1
            #j += 1
            #k += 1
	# 한쪽에 남아 있는 레코드의 일괄 복사
    if i > mid :
        sorted[k:k+right-j+1] = A[j:right+1]
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]
	# 배열 sorted[]의 리스트를 배열 list[]로 다시 복사
    A[left:right+1] = sorted[left:right+1]



############################################################
# 테스트 프로그램
if __name__ == "__main__":
    data = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]
    print("Original  : ", data)
    merge_sort(data, 0, len(data)-1)
    print("Merge     : ", data)
