class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        start = 0
        end = len(letters) - 1
        if target < letters[start]:
            return letters[start]
        if target >= letters[end]:
            return letters[0]
        while start <= end:
            mid = (start + end) // 2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        return letters[start]