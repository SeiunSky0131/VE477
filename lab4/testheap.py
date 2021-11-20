import fibonacci_heap

Heap = fibonacci_heap.FiboHeap()
Heap2 = fibonacci_heap.FiboHeap()
a = fibonacci_heap.FiboNode(17)
b = fibonacci_heap.FiboNode(30)
c = fibonacci_heap.FiboNode(24)
d = fibonacci_heap.FiboNode(26)
e = fibonacci_heap.FiboNode(46)
f = fibonacci_heap.FiboNode(35)
g = fibonacci_heap.FiboNode(23)
h = fibonacci_heap.FiboNode(7)
i = fibonacci_heap.FiboNode(3)
j = fibonacci_heap.FiboNode(18)
k = fibonacci_heap.FiboNode(39)
l = fibonacci_heap.FiboNode(52)
m = fibonacci_heap.FiboNode(41)
n = fibonacci_heap.FiboNode(44)
o = fibonacci_heap.FiboNode(99)
p = fibonacci_heap.FiboNode(101)
q = fibonacci_heap.FiboNode(102)
input = [a,b,c,d,e,f,g,h,i,j,k,l,m,n]
input2 = [o,p,q]

#Test both Insert and MakeHeap -> finished rightly----------------------------------------------
# for element in input:
#     Heap.Insert(element)
# Heap.Insert(a)
Heap.MakeHeap(input)
Heap2.MakeHeap(input2)

Heap.PrintFiboHeap()
print("Insert complete!")

#DecreaseKey test ->  finished rightly ----------------------------------------------------------
node = Heap.FindNode_in_FiboHeap(30)
Heap.DecreaseKey(node,1)
Heap.PrintFiboHeap()

node = Heap.ExtractMin()
print("extracted node is:",node.key)
Heap.PrintFiboHeap()

print("Now decrease 35 to 25, this does not violate the min heap")

node = Heap.FindNode_in_FiboHeap(35)
Heap.DecreaseKey(node,25)
Heap.PrintFiboHeap()

print("Further decrease 25 to 2, this violate the min heap, call a Cut and a Cuscut")
node = Heap.FindNode_in_FiboHeap(25)
Heap.DecreaseKey(node,2)
Heap.PrintFiboHeap()

print("Check whether 23 is marked")
node = Heap.FindNode_in_FiboHeap(23)
if(node.marked == True):
    print("23 is marked")
else:
    print("23 is not marked")

print("decrease the 26 to 1, this will result in a Cascut, cut 23 off")
node = Heap.FindNode_in_FiboHeap(26)
Heap.DecreaseKey(node,1)
Heap.PrintFiboHeap()

print("check whether 3 is marked, it should not be marked")
node = Heap.FindNode_in_FiboHeap(3)
if (node.marked == True):
    print("3 is marked")
else:
    print("3 is not marked")

# Test Delete -> finished rightly------------------------------------------------------------
print("Now delete 41")
node = Heap.FindNode_in_FiboHeap(41)
Heap.Delete(node)
Heap.PrintFiboHeap()

# Test Union
print("Now Union with the second Heap")
Heap.Union(Heap2)
Heap.PrintFiboHeap()


# ExtractMin test -> finished rightly ------------------------------------------------
# node = Heap.ExtractMin()
# print("extracted node is:",node.key)
# Heap.PrintFiboHeap()

# node = Heap.ExtractMin()
# print("extracted node is:",node.key)
# Heap.PrintFiboHeap()

# node = Heap.ExtractMin()
# print("extracted node is:",node.key)
# Heap.PrintFiboHeap()

# node = Heap.ExtractMin()
# print("extracted node is:",node.key)
# Heap.PrintFiboHeap()

# node = Heap.ExtractMin()
# print("extracted node is:",node.key)
# Heap.PrintFiboHeap()
