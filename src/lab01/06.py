N = int(input())
c_True = c_False = 0
for i in range(N):
    name = input().split()
    if name[-1] == "True":
        c_True += 1
    else:
        c_False += 1
print(c_True, c_False)
