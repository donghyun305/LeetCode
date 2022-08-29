def isValid(s: str) -> bool:
    s = list(s)
    sum = []
    val = {')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in val.values():
            sum.append(i)
        else:
            if sum and val[i] == sum[-1]:
                sum.pop()
            else:
                return False
    if sum:
        return False
    else:
        return True


    # while len(s) >= 2:
    #     if s[0] == '(' and s[1] == ')':
    #         s.remove(s[0])
    #         s.remove(s[0])
    #         sum += 2
    #     elif s[0]== '[' and s[1] == ']':
    #         s.remove(s[0])
    #         s.remove(s[0])
    #         sum += 2
    #     elif s[0]== '{' and s[1] == '}':
    #         s.remove(s[0])
    #         s.remove(s[0])
    #         sum += 2
    #     else:
    #         return False
    #
    # if sum == length:
    #     return True
    # else:
    #     return False

print(isValid('({)}[]'))



