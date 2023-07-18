def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_num = sequence[i-1] + sequence[i-2]
            sequence.append(next_num)
        return sequence

fibonacci_sequence = __import__('fibonacci_sequence').fibonacci_sequence

print(fibonacci_sequence(10))
print(fibonacci_sequence(5))
print(fibonacci_sequence(0))
print(fibonacci_sequence(1))