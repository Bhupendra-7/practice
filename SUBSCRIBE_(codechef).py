def Find_cost(N,X):
    if N != 0 and N < 2:
        return X
    elif N <= 6:
        return X
    elif N % 6 == 0:
        return X * (N // 6)
    else:
        return X * ((N // 6) + 1)
        
            
# T = int(input())

# for _ in range(T):
#     N, X = map(int, input().split())
#     print(Find_cost(N, X))