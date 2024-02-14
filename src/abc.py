def create(n):
 
    numbers = []
    for i in range(1,n+1):
        numbers.append(i)
    if len(numbers) == 1:
        return numbers
 
    order = []
    i = 1
    while(len(numbers)>0):
        if len(numbers) == 1:
            order.append(numbers[0])
            break
        elif i == len(numbers):
            i = 0
        elif i > len(numbers):
            i = 1
        order.append(numbers.pop(i))
        i += 1
    return order
 
if __name__ == "__main__":
 
    print(create(1)) # [1]
    print(create(2)) # [2,1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(8))

