from typing import List

def longestCommonPrefix(strs: List[str]):
    strs.sort(key=lambda x : len(x))

    if len(strs) == 0 or len(strs) == 1:
        return ""
    else:
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        return strs[0]

print(longestCommonPrefix(['flower', 'fly', 'fldasdas']))
