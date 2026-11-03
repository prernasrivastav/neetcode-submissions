class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1st Approach : Sorting
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        # 2nd Approach : counting
        # return Counter(s) == Counter(t)

        # 3rd Approach : Hash Map
        # if len(s) != len(t):
        #     return False

        # countS, countT = {}, {}

        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        # return countS == countT