def roman(s: str):
    man = {'I': '1', 'IV':'4', 'V' :'5', 'IX':'9', 'X' : '10', 'XL':'40', 'L':'50', 'XC':'90', 'C':'100','CD':'400',
           'D':'500', 'CM':'900' ,'M':'1000'}
    s = list(s)
    sum = 0
    point = 0
    while point < len(s):
        if point + 1 < len(s) and (s[point] + s[point+1]) in man:
            sum += int(man[s[point] + s[point+1]])
            point += 2
        else:
            sum += int(man[s[point]])
            point += 1
    return sum
print(roman('MCMXCIV'))




    # while s:
    #     if len(s) == 1:
    #         sum += int(man[s[0]])
    #         return sum
    #
    #     if s[0]=='I' or s[0]== 'X' or s[0]=='C':
    #         if s[0]=='I' and (s[1]=='V' or s[1]=='X'):
    #             sum = sum + int(man[s[1]]) - int(man[s[0]])
    #             s.remove(s[0])
    #             s.remove(s[0])
    #         elif s[0]=='X' and (s[1]=='L' or s[1]=='C'):
    #             sum = sum + int(man[s[1]]) - int(man[s[0]])
    #             s.remove(s[0])
    #             s.remove(s[0])
    #         elif s[0] == 'C' and (s[1] == 'D' or s[1]=='M'):
    #             sum = sum + int(man[s[1]]) - int(man[s[0]])
    #             s.remove(s[0])
    #             s.remove(s[0])
    #         else:
    #             sum += int(man[s[0]])
    #             s.remove(s[0])
    #     else:
    #         sum += int(man[s[0]])
    #         s.remove(s[0])
    #
    # return sum




#     if s[0] == 'I' or s[0] == 'X' or s[0] == 'C':
#         sum += int(man[s[0]])
#         s.remove(s[0])
#         while s:
#             if sum >= int(man[s[0]]):
#                 sum += int(man[s[0]])
#                 s.remove(s[0])
#             else:
#                 if sum < int(man[s[0]]):
#                     sum = int(man[s[0]]) - sum
#                     s.remove(s[0])
#
#     else:
#         while s:
#             sum += int(man[s[0]])
#             s.remove(s[0])
#         return sum
#     return sum
#
# print(roman('MCMXCIV'))
#
#
#
