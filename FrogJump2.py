def solution(X, A):
    checker=0
    final_val=pow(2,X)-1
    for x in range(len(A)):
        checker=checker| 1<<(A[x]-1)
        if(checker==final_val):
            return x
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
