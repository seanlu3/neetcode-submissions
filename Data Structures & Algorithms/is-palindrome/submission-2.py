class Solution:
    def isPalindrome(self, s: str) -> bool:

        arr = []

        for i in s:
            if i.isalnum():
                arr.append(i.lower())

        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
