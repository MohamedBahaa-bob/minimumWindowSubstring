# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


def allZeros(array):
    for i in range(0, 58):
        if array[i] != 0:
            return False
    return True


def isValid(array, charsT):
    i = 0
    while i in range(len(charsT)):
        if array[i] < charsT[i]:
            return False
        i += 1
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if m < n:
            return ""
        charsT = [0] * 58
        appearances = [0] * 58
        checkpoints = []
        for i in range(0, n):
            charsT[ord(t[i]) - 65] += 1
        copiedT = copy.deepcopy(charsT)
        l, r = 0, 0
        valid = False
        saveR = 0
        while r < m:
            if copiedT[ord(s[r]) - 65] != 0:
                copiedT[ord(s[r]) - 65] -= 1
            if charsT[ord(s[r]) - 65] != 0:
                checkpoints.append(r)
                # appearances[ord(s[r]) - 65] += 1
            if not valid and allZeros(copiedT):
                saveR = r + 1
                valid = True
            r += 1
        if valid:
            l = checkpoints.pop(0)
            minSolution = s[l:saveR]
        else:
            return ""
        print(checkpoints)
        c = s[l]
        r = 0
        while r < m:
            if charsT[ord(s[r]) - 65] != 0:
                appearances[ord(s[r]) - 65] += 1
                if c == s[r]:
                    while appearances[ord(c) - 65] > charsT[ord(c) - 65] and len(checkpoints) > 0:
                        appearances[ord(c) - 65] -= 1
                        l = checkpoints.pop(0)
                        # print(l)
                        c = s[l]
            # print(isValid(appearances,charsT))
            if isValid(appearances, charsT) and len(s[l:r + 1:]) < len(minSolution):
                minSolution = s[l:r + 1:]
            r += 1
        if r == m and len(checkpoints) > 0:
            while checkpoints and appearances[ord(c) - 65] > charsT[ord(c) - 65]:
                appearances[ord(c) - 65] -= 1
                l = checkpoints.pop(0)
                c = s[l]
        if isValid(appearances, charsT) and len(s[l:r:]) < len(minSolution):
            minSolution = s[l:r:]
        return minSolution


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
