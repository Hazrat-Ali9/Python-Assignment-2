N,M = map(int, input().split())

num = list(map(int, input().split()))

freq_arry = [0] * (M + 1)

for i in num:
    freq_arry[i] += 1
    
for values in freq_arry[1:]:
    print(values)
