
def solve():
    X = int(input())
    if X <= 7:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()


