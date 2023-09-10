def raise_power(base_num, power_num):
    result = 1
    for _ in range(power_num):
        result *= base_num
    return result

input_str = input("Enter a base number and a power number separated by a space: ")
input_list = input_str.split()

# Extract the base number and power number from the input list
base_num = int(input_list[0])
power_num = int(input_list[1])

# Call the raise_power function with the user-input values
result = raise_power(base_num, power_num)
print("Result:", result)
