def solution(A):
    P = 1
    N = len(A)
    L = sum(A[:P])
    R = sum(A[P:])
    minimal_difference = abs(L - R)
    for P in range(2, N):
        current = A[P - 1]
        L += current
        R -= current
        minimal_difference = min(minimal_difference, abs(L - R))
    return minimal_difference

#exam = [3,1,2,4,3]
#print(solution(exam))
