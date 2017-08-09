def minion_game(string):
    # # MY FIRST ATTEMPT BUT TOO LONG FOR LONG STRINGS
    # def vowel(chr):
    #     res = False
    #     if chr in 'aeiouy' or chr in 'AEIOUY':
    #         res = True
    #     return res
    #
    # string = string.lower()
    # a = [string[i] for i in range(len(string))]
    # vowrep = []
    # nvowrep = []
    #
    # for i in range(len(a)):
    #     if vowel(a[i]):
    #         vowrep.append(i)
    #     else:
    #         nvowrep.append(i)
    # k = 0
    # l = 0
    # for i in range(len(vowrep)):
    #     for j in range(vowrep[i], len(a)):
    #         # print(a[vowrep[i]:j+1])
    #         k = k + 1
    # for i in range(len(nvowrep)):
    #     for j in range(nvowrep[i], len(a)):
    #         # print(a[nvowrep[i]:j+1])
    #         l = l + 1
    #
    # if k > l:
    #     print('Kevin', k)
    # elif k < l:
    #     print('Stuart', l)
    # elif k == l:
    #     print('Draw')
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(s) - i)
        else:
            stusc += (len(s) - i)

    if kevsc > stusc:
        print("Kevin", kevsc)
    elif kevsc < stusc:
        print("Stuart", stusc)
    else:
        print("Draw")

s = input()
minion_game(s)