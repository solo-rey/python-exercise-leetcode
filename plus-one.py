# @param digits, a list of integer digits
# @return a list of integer digits
def plusOne(digits):
    digits = digits[::-1]
    carry = 1
    for i in range(len(digits)):
        digits[i]+=carry
        carry = digits[i] / 10
        digits[i] %= 10
    if carry == 1:
        digits.insert(len(digits),carry)
    return digits[::-1]