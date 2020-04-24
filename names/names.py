import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('/home/ehoover/Sprint-Challenge--Data-Structures-Python/names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('/home/ehoover/Sprint-Challenge--Data-Structures-Python/names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the duplicates to this duplicate data structure

tree = BinarySearchTree('please')

# go through the contents of names_1.txt, adding them to the "tree"
# then go through the contents of names_2.txt and use the 'contains' BST method
# if the name is also found in the tree (contents of names_1.txt)
# then append to the duplicates list

for i in names_1:
    tree.insert(i)

for j in names_2:
    if tree.contains(j):
        duplicates.append(j)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
