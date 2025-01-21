arr = [100, 115, 90, 120, 85, 130]
temp = 0
profit = 0
counter = 0
for number in arr:
    for number_to_compare in arr:
        counter += 1
        profit = number_to_compare - number
        print(f"profit can be {counter}: ", profit)
        if profit > temp:
            temp = profit

print("the max profit can be: ", temp)
