my_list = []
# appending of the following elements to may_list 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15)
# extend my_list
my_list.extend([50,60,70])
#Remove the last element from my_lis
my_list.pop()
#Sort my_list in ascending order
my_list.sort()
#Find and print the index of the value 30 in my_list
index_30 = my_list.index(30)
print(f"the indexof 30 in my_list is: {index_30}")