input_set1 = input("Enter a number for the first set (separated by spaces): ")
set1 = set(map(int, input_set1.split()))
input_set2 = input("Enter a number for the second set (separated by spaces): ")
set2 = set(map(int, input_set2.split()))
common_elements = set1.intersection(set2)
print("Common elements between the two sets:")
for element in common_elements:
    print(element)

    