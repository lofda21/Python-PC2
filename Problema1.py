start = 1500
end = 2700
result = [num for num in range(start, end + 1) if num % 7 == 0 and num % 5 == 0]
print(result)
