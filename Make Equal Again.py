from collections import Counter
t = int(input())
ans = []
def test():
    n = int(input())
    elements = []
    for c in input().split(" "):
        elements.append(int(c))
    c = Counter(elements)
    print(n)

for i in range(t):
    test()
