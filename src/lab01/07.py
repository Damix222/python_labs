s = input()
s_new = ""
alph = "QWERTYUIOPASDFGHJKLZXCVBNM"
index_1 = 894537858347598347598347598347958
for word in alph:
    if 0 < s.find(word) < index_1:
        index_1 = s.find(word)
index_2 = 583475893475349857
for i in range(len(s)):
    if s[i].isdigit():
        index_2 = min(index_2, i)
step = index_2 + 1 - index_1
for x in range(index_1, len(s) + 1, step):
    s_new += s[x]
print(s_new)
