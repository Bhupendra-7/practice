# cook your dish here
def isPassed(x,y,z):
    school_students = x * y
    if z > (school_students // 2):
        return 'YES'
    else:
        return 'NO'
        
        
        
# T = int(input())  # number of test cases

# for _ in range(T):
#     x, y, z = map(int, input().split())
#     print(isPassed(x, y, z).upper())  # call your function and print in uppercase