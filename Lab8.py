# Program Name: Lab8.py 
# Course: IT1114/Section 01
# Student Name: Trabian Ferguson
# Assignment Number: Lab8.py
# Due Date: 10/22/2023
# Purpose: This program will combine two integer arrays into one larger array and remove duplicate values

from random import randint

def random_array(length):
    return [randint(0, 500) for _ in range(length)]

def random_arraysfunc():
    num_elements = int(input("N:"))
    if num_elements < 2:
        return None
    first_array = random_array(num_elements)
    second_array = random_array(num_elements)
    return first_array, second_array

def merge_remove_dupes(array1, array2):
    merged_array = list(set(array1 + array2))
    merged_array.sort()
    return merged_array

def main():
    random_arrays = random_arraysfunc()
    if random_arrays is None:
        return

    combine_array = merge_remove_dupes(random_arrays[0], random_arrays[1])

    num_dupes = len(random_arrays[0]) + len(random_arrays[1]) - len(combine_array)
    print("Number of dupes in the merged array:", num_dupes)

    print("Sorted merged array:", combine_array)

if __name__ == "__main__":
    main()







