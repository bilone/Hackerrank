s = input()
# Alnum=False
# Alpha=False
# Digit=False
# Low=False
# Up=False
#
# for i in range (len(s)):
#     if s[i].isalnum():
#         Alnum=True
#     if s[i].isalpha():
#         Alpha=True
#     if s[i].isdigit():
#         Digit=True
#     if s[i].islower():
#         Low=True
#     if s[i].isupper():
#         Up=True
#
#
#
#
# print(Alnum)
# print(Alpha)
# print(Digit)
# print(Low)
# print(Up)

#A simple Method

print(any(x.isalnum() for x in s))
print(any(x.isalpha() for x in s))
print(any(x.isdigit() for x in s))
print(any(x.islower() for x in s))
print(any(x.isupper() for x in s))