class Solution:
    def getSum(self, x: int, y: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while y != 0:
            carry = (x & y) << 1
            x = (x ^ y) & mask
            y = carry & mask
        return x if x <= max_int else ~(x ^ mask)
        

        