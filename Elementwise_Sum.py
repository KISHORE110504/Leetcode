"""Elementwise Sum
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples."""

def tuple_elementwise_sum(t1, t2):
    return tuple(map(sum, zip(t1, t2)))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)