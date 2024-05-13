# Given code
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Counting operators and operands
operators = ['=', '^', 'for', 'in', 'return']
operands = ['singleNumber', 'nums', 'result', 'num']

N = len(operators) + len(operands)  # Halstead Length

# Counting unique operators and operands
unique_operators = set(operators)
unique_operands = set(operands)
n = len(unique_operators) + len(unique_operands)  # Vocabulary (n)

# Computing Halstead Volume
V = N * (log2(n)) if n > 0 else 0

print("Halstead Length (N):", N)
print("Halstead Volume (V):", V)
