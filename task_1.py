

# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_element = 4

sum_values = sum(numbers[:missing_element ]) + sum(numbers[missing_element+1:])
number_elements = len(numbers)
average_value = sum_values / number_elements

numbers[missing_element] = average_value
print("Измененный список:", numbers)

