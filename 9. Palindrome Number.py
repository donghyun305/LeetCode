# a = int(121)
# b = str(a)
# print(b[1])


# x = [1,2,3,4]
# print(x[::-1])
# # class Solution:
# def isPalindrome(x: int) -> bool:
#     y = str(x)
#     for i in range(len(y)):
#         if y[i] == y[len(y)-i-1]:
#             return True
#         else:
#             return False
#
# isPalindrome(1234321)
def pol(x:int):
    ret=None

    if x<0:
        ret = False
    else:
        original = x
        reverse = 0
        while x :
            remainder = x%10
            x = x//10
            reverse=reverse*10 + remainder

        if reverse == original:
            ret = True
        else:
            ret = False
    return ret

pol(1234)
