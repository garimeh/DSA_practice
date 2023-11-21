class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        queue = list(range(1, 10))
        while queue:
            num = queue.pop(0)
            if num > high:
                break
            if low <= num <= high:
                result.append(num)
            last_digit = num % 10
            if last_digit < 9: 
                queue.append(num * 10 + last_digit + 1)
        return result