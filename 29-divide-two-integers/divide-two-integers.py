class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        a = abs(dividend)
        b = abs(divisor)

        result = 0

        # Subtract powers of 2
        while a >= b:
            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            result += multiple

        # Apply sign
        if negative:
            result = -result

        # Clamp to 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, result))