def solution(A):
    return int(min(A) == 1 and max(A) == len(A) == len(set(A)))
    
print(solution([4,2,1,3]))
print(solution([4,1,1,3]))
print(solution([4,2,1,4]))
print(solution([4,2,5,3]))
