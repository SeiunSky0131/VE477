import math
class FiboNode:
    def __init__(self, key_t):
        self.parent = None
        self.child = None    #The first child of this node
        self.left = self
        self.right = self
        self.key = key_t     #key value
        self.degree = 0      #number of children of this node
        self.marked = False  #used for deletion
    
    #insert the childnode as the child of a FiboNode
    def insertChild(self, childnode):
        childnode.parent = self #set the parent of childnode to be self
        self.degree = self.degree + 1

        #if self does not have a child, set the childnode as the first child
        if self.child == None:
            self.child = childnode

            #note that when we insert a node, we need to update its left and right, this is required to be an invariant
            childnode.left = childnode
            childnode.right = childnode

        #else we need to insert the child at the left of the first child, which is also at the end of the linked list
        else:
            childnode.right = self.child
            childnode.left = self.child.left
            self.child.left.right = childnode
            self.child.left = childnode
    
    # REQUIRE: This node is the left most node in the linked list
    # print the key following nodes in the order:
    # 1. This node
    # 2. All this node's children (in the recursive manner)
    # 3. The next brother of this node
    # 4. All the children of next brother of this node
    # 5. ...
    def printNode(self):
        curr_node = self        #set current node to be the left most node in the linked list
        end_node = self.left    #set the end node to be the node left to current node
        while True:
            print(curr_node.key)         #print this node

            if curr_node.child != None:       #if the node has child, just call this function recursively  
                curr_node.child.printNode()
                
            if curr_node == end_node:
                break
            else:
                curr_node = curr_node.right

    #return the node with key = key_t in the heap with the left most node in the root linked list to be self
    #return None if the node is not found
    def Find_Node_by_Key(self, key_t):      
        curr_node = self            #set the current node to be the left most node in the root linked list
        end_node = self.left        #set the end node to be the left of current node
        # print("curr_node is:", curr_node.key)
        # print("end_node is:", end_node.key)

        while True:
            # print("curr_node in the loop is:",curr_node.key)
            #if the current node has the key, then we are done
            if(curr_node.key == key_t): 
                return curr_node
            
            #if the we search all the children of current node and we find the key, then we are done
            if(curr_node.child != None): 
                result = curr_node.child.Find_Node_by_Key(key_t)
                if (result != None):
                    return result
                
            #otherwise we need to seek for its brothers
            #if we have already visited all the brothers and the function is still alive, we have no such key
            #else we go to the next brother
            if(curr_node == end_node):
                return None
            else:
                curr_node = curr_node.right

class FiboHeap:
    def __init__(self):
        self.min = None    #The minimum node in the FiboHeap, note that it must be in the root linked list
        self.NodeNum = 0   #The number of node in the FiboHeap
        self.maxDegree = 0 #The maximum degree of node in the heap

    #Return true if the FiboHeap is empty
    def isEmpty(self):
        return (self.min == None)

    #REQUIRE: The array is not empty, composed of element in type FiboNode
    #But we still add the component to judge whether the list is not empty
    #Make a Fibonacci Heap using the elements in the array, by inserting all the elements in the root linked list
    def MakeHeap(self, list_t):
        if list_t:                     #if the list is not empty
            for element in list_t:

                #if the root linked list is empty, simply insert it at beginning
                if (self.min == None):
                    # print("first node inserted!")
                    self.min = element
                    element.left = element
                    element.right = element

                    #update the NodeNum, maxDegree
                    self.NodeNum = self.NodeNum + 1
                    self.maxDegree = element.degree #actually no need, since the maxdegree is 0 in this case

                #if the root linked list is non-empty, insert it at the left of the min node (regarded as end of list)
                else:
                    # print("self.min is now:",self.min.key)
                    element.right = self.min
                    element.left = self.min.left
                    self.min.left.right = element
                    self.min.left = element

                    #update the min, NodeNum, maxDegree
                    if (element.key < self.min.key):
                        self.min = element
                    self.NodeNum = self.NodeNum + 1
                    if (self.maxDegree < element.degree): #actually no need, since the maxdegree is 0 in this case
                        self.maxDegree = element.degree

    #Return the minimum node in the FiboHeap, return None if the FiboHeap is empty
    def Minimum(self):
        return self.min

    #REQUIRE: both this heap and another_heap is not empty
    #But we still add the component to judge whether the heap is empty
    #Link two FiboHeap together, note that only this heap is modified, the other heap remains the same
    #The method to do this is just link the root linked list of them
    def Union(self, another_heap):

        #if this heap is empty and the other heap is not empty
        if(self.isEmpty() == True and another_heap.isEmpty() == False ):

            #set the parameters
            self.min = another_heap.min
            self.NodeNum = another_heap.NodeNum
            self.maxDegree = another_heap.maxDegree

        #if this heap is not empty and the other heap is not empty
        if(another_heap.isEmpty() == False):
            head_1 = self.min
            tail_1 = self.min.left
            head_2 = another_heap.min
            tail_2 = another_heap.min.left

            head_1.left = tail_2
            tail_1.right = head_2
            head_2.left = tail_1
            tail_2.right = head_1

            #set the parameters
            if(another_heap.min.key < self.min.key):
                self.min = another_heap.min

            self.NodeNum = self.NodeNum + another_heap.NodeNum

            if(another_heap.maxDegree > self.maxDegree):
                self.maxDegree = another_heap.maxDegree
            
    #Extract the minimum element in the FiboHeap
    #By putting the children of this nodes into the root linked list and consolidate the trees
    #first put all the nodes to the root linked list(if any), then update and consolidate
    def ExtractMin(self):
        victim = self.min

        if (victim != None):

            #if it has child, insert all the children to the left of victim
            if(victim.child != None):
                curr_node = victim.child
                end_node = victim.child.left
                # print("curr_node is:",curr_node.key)
                # print("end_node is:", end_node.key)

                while True:
                    flag_end = False
                    if(curr_node == end_node):
                        flag_end = True
                    #print("potential deadlock")
                    # print("curr_node is:", curr_node.key)
                    curr_node.parent = 0 #erase the parent of this child
                    next_child = curr_node.right #update the next child to be melted
                    curr_node.left = self.min.left
                    curr_node.right = self.min
                    self.min.left.right = curr_node
                    self.min.left = curr_node

                    if(flag_end == True):
                        break
                    else:
                        curr_node = next_child

            #if the victim is the only node in the rooted linked list and having no child
            if(victim.right == victim):
                self.min = None
                self.NodeNum = 0
                self.maxDegree = 0
                return victim

            #else if the victim is not the only node, then delete the victim from the root linked list
            victim.left.right = victim.right
            victim.right.left = victim.left
            victim.child = None

            curr_node = victim.right
            end_node = victim.left 
            temp_min = curr_node
            maxDegree = curr_node.degree

            while True:

                #update the temp_min
                if(curr_node.key < temp_min.key):
                    temp_min = curr_node
                #update the maxDegree
                if(curr_node.degree > maxDegree):
                    maxDegree = curr_node.degree

                if(curr_node == end_node):
                    break
                else:
                    curr_node = curr_node.right

            self.min = temp_min
            # print("The new min is:",self.min.key)
            self.NodeNum = self.NodeNum - 1
            self.Consolidate() #maxDegree is updated here
            return victim

    #Insert a FiboNode into the FiboHeap
    #By putting this node at the left of the min 
    def Insert(self, node_t):

        #If the FiboHeap is empty, simply insert the node at the min
        if(self.isEmpty() == True):
            self.min = node_t

            #maintain the parameters
            self.NodeNum = self.NodeNum + 1
            self.maxDegree = 0
    
        #Else we insert it at the left of the min node
        else:
            node_t.left = self.min.left
            node_t.right = self.min
            self.min.left.right = node_t
            self.min.left = node_t

            #maintain the parameters, note that insert will not increase the maxDegree
            self.NodeNum = self.NodeNum + 1
            if(self.min.key > node_t.key):
                self.min = node_t

    #This function operate on the root linked list so that no heaps have the same degree
    #By melting heaps together
    #update the maxDegree is finished as well
    def Consolidate(self):

        #declare an array and initialize all the elements to None
        rank_list = []
        for i in range(0, self.NodeNum):
            rank_list.append(None)
        #print("listsize is:", len(rank_list))
        
        #set the current node to be the min node of the FiboHeap
        #set the end node to be the left of the min node of the FiboHeap
        curr_node = self.min
        end_node = self.min.left

        #begin the loop, from curr_node to end_node
        #first analyze then update
        while True:
            flag_end = False
            if(curr_node == end_node):
                flag_end = True
            #print("curr_node degree is:", curr_node.degree)

            #if the corresponding bucket is None, then we are fine, just make that pointer pointing to current node
            if(rank_list[curr_node.degree] == None):
                rank_list[curr_node.degree] = curr_node
                #print(curr_node.key, "insert into a new bucket with index:", curr_node.degree)

            #else, the corresponding bucket has some node, then we need to call Link
            #And then we continue to try, until we can find a bucket with node input
            #Then we insert the newly built node to that bucket 
            #Be cautious about the order of calling Link
            else:
                #print(curr_node.key, "has curr_node degree:",curr_node.degree)
                while(rank_list[curr_node.degree] != None):
                    #mark down the intial bucket, it should be cleared after the link operation
                    index = curr_node.degree
                    curr_node = self.Link(rank_list[curr_node.degree], curr_node)
                    rank_list[index] = None
                    #print (curr_node.key, "has curr_node degree:",curr_node.degree, "after combine" )
    
                
                #The while loop ends, then we are able to insert to bucket
                rank_list[curr_node.degree] = curr_node

            if(flag_end == True):
                break
            else:
                curr_node = curr_node.right

        #update the maxDegree
        #find the first element that is not None in the reversed rank_list, which should be the element with biggest rank
        for element in reversed(rank_list):
            if(element != None):
                self.maxDegree = element.degree
                break

    #INPUT: two root nodes that have the same rank, and they are still in the root linked list
    #Link two nodes based on the key of root node, the node with smaller key will be the new root
    #And the newly linked heap will be located at the original postion of node_y
    #RETURN: return a pointer pointed to the new root
    def Link(self, node_x, node_y):
        
        #cut off node x
        node_x.left.right = node_x.right
        node_x.right.left = node_x.left

        #if x > y, simply link x to y
        if(node_x.key > node_y.key):
            node_y.insertChild(node_x)
            return node_y

        #else x <= y, change the pointers and link y to x
        else:
            node_x.left = node_y.left
            node_x.right = node_y.right
            node_y.left.right = node_x
            node_y.right.left = node_x
            node_x.insertChild(node_y) 
            return node_x

    #Decrease the key of node_t to key_t
    #REQUIRE: The new key_t is smaller than the original key
    def DecreaseKey(self, node_t, key_t):
        #If invalid input, do nothing
        if(node_t.key <= key_t):
            return
        
        #Else we first change the value of the node_t
        node_t.key = key_t

        #if the key violate the min_heap principle
        #Do a cut to this node, do a cascut to its parent
        if(node_t.parent != None and node_t.key < node_t.parent.key):

            #note that the parent of node_t will be changed in the Cut, so we store it in advance
            parent_node = node_t.parent
            self.Cut(node_t)
            self.CasCut(parent_node)
            return

        #else we consider update the min node
        if(node_t.key < self.min.key):
            self.min = node_t
            return

    #Cut the heap rooted at node_t and melt it into the root linked list
    def Cut(self, node_t):
        #if the parent of node_t only has this child
        if(node_t.parent.degree == 1):
            node_t.parent.child = None
            node_t.parent.degree = 0
            node_t.parent = None

            #melt it into the root linked list
            node_t.left = self.min.left
            node_t.right = self.min
            self.min.left.right = node_t
            self.min.left = node_t

            #update min
            if(node_t.key < self.min.key):
                self.min = node_t

            #unmark the node_t
            node_t.marked = False

        #else, having more than one child
        else:

            #if node_t is the first child of its parent, delete it, change the child
            if(node_t.parent.child == node_t):
                node_t.right.left = node_t.left
                node_t.left.right = node_t.right
                node_t.parent.child = node_t.right

            #else node_t is not the first child of its parent, delete it
            else:
                node_t.right.left = node_t.left
                node_t.left.right = node_t.right
            
            #decrement the parent's degree
            node_t.parent.degree = node_t.parent.degree - 1
            #erase the parent of node_t
            node_t.parent = None

            #insert the node into the root linked list, at the left of the min node, update min, and unmark the node_t
            node_t.left = self.min.left
            node_t.right = self.min
            self.min.left.right = node_t
            self.min.left = node_t

            #update min
            if(node_t.key < self.min.key):
                self.min = node_t

            #unmark the node_t
            node_t.marked = False

    #CasCut the heap from the node_t, note that if the node_t is originally not marked->mark it
    #else, cut it off and melt in the root node list
    #and CasCut it parent
    def CasCut(self, node_t):
        #if the node_t is a root node, we do nothing
        if(node_t.parent == None):
            return

        #else if the node_t is not a root node and it is not marked, mark it
        if(node_t.marked == False):
            node_t.marked = True
            return
        
        #else if node_t is marked, cut it off and melt it into the root linked list
        if(node_t.marked == True):

            #note that Cut will change the parent of node_t to None, should store it beforehand
            parent_node = node_t.parent
            self.Cut(node_t)

            #recursive call
            self.CasCut(parent_node)

    #Delete a FiboNode type element, if there is no such element, do nothing
    #Delete is just a combination of DecreaseKey and ExtractMin
    def Delete(self, node_t):
        if(node_t == None):
            return
        else:
            self.DecreaseKey(node_t, (self.min.key - 1))
            self.ExtractMin()

    #Print the structure of the FiboHeap
    def PrintFiboHeap(self):
        self.min.printNode()

    #Return a pointer to a node with key to be key_t
    def FindNode_in_FiboHeap(self, key_t):
        return self.min.Find_Node_by_Key(key_t)
        
