class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def addOne(digits, index):
            num = digits[index] + 1
            if num <= 9:
                digits[index] = num
            else:
                digits[index] = 0
                if abs(index - 1) <= len(digits):
                    addOne(digits, index - 1 )
                else:
                    digits.insert(0, 1)
        addOne(digits, -1)
        return digits
        