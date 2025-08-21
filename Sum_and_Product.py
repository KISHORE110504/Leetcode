"""Sum and Product
Write a function that calculates the sum and product of all elements in a tuple of numbers."""

#This is a tuple coding challenge


def sum_product(input_tuple):
    product_result = 1
    if input_tuple != 0:
        sum_result = sum(input_tuple)
        for n in input_tuple:
            product_result *= n
    return sum_result, product_result

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)
