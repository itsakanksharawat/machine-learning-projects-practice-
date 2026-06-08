numbers = [5,2,1,7,4]
for i in range(len(numbers) - 1):
    if(numbers[i] == numbers[i+1]):
        numbers.remove(numbers[i])
print(numbers)
