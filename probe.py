s, s1 = 'abcddfff', ''
a = 0
n = s[0]
for i in s:
    if n == i:
        a += 1
    else:
        s1 += (n + str(a))
        a = 1
        n = i
s1 += (n + str(a))
print(s1)

# end_s = ""
# i = -1 * len(s)
# while i < 0:
#     k = 1
#     if s[i] == s[i+1]:
#         while s[i] == s[i+1] and i < -1:
#             i = i + 1
#             k = k + 1
#         end_s = end_s + s[i] + str(k)
#         i = i + 1
#     else:
#         end_s = end_s + s[i] + str(k)
#         i = i + 1
# print(end_s)
