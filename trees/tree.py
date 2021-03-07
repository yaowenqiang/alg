from collections import deque
class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def get_value(self):
        return self.value

    def set_value(self,value):
        self.value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self,node):
        self.left = node

    def get_right_child(self):
        return self.right

    def set_right_child(self,node):
        self.right = node
    
    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

class Tree(object):
    def __init__(self,value = None):
        if value != None:
            self.root = Node(value)
    
    def get_root(self):
        return self.root

    def compare(self, node, new_node):
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    def insert_with_loop(self, new_value):
        new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                node.set_value(new_node.get_value())
                break
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break
    
    def insert_recursively(self, noew, new_node):
        comparison == self.compare(node, new_node)
        if comparison == 0:
            node.set_value(new_node.get_value())
        elif comparison == -1:
            if node.has_left_child():
                self.insert_recursively(node.get_left_child(), new_node)
            else:
                node.set_left_child(new_node)
        else:
            if node.has_right_child():
                self.insert_recursively(node.get_right_child(), new_node)
            else:
                node.set_right_child(new_node)


    def search(self, value):
        node = self.get_root()
        s_node = Node(value)
        while(True):
            comparison = self.compare(node, s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False

    def delete(self, value):
        node = self.get_root()
        s_node = Node(value)
        if node == None:
            return node
        while(True):
            comparison = self.compare(node, s_node)
            if comparison == 0:
                matched = True
                break
            elif comparison == -1:
                if node.has_left_child():
                    parentNode = node
                    node = node.get_left_child()
                else:
                    matched = False
                    break
            else:
                if node.has_right_child():
                    parentNode = node
                    node = node.get_right_child()
                else:
                    matched = False
                    break
        
        if matched == True:
            if node.has_left_child() == True:
                # has two child
                if node.has_right_child() == True:
                    currentNode = node
                    while (currentNode.has_left_child()):
                        parentCurrentNode = currentNode
                        currentNode = currentNode.get_left_child()

                    node.set_value(currentNode.get_value()) 
                    parentCurrentNode.set_left_child(parentCurrentNode.get_right_child())
                    currentNode.set_value(None)
                # only has one child
                else:
                    parentNode.set_left_child(node.get_left_child())
                    node.set_value(None)
            else:
                # has no child
                if node.has_right_child():
                    rightChild = node.get_right_child()
                    node.set_value(rightChild.get_value())
                    if rightChild.has_left_child():
                        node.set_left_child(rightChild.get_left_child())
                    if rightChild.has_right_child():
                        node.set_right_child(rightChild.get_right_child())
                else:
                    node.set_value(None)


        # pass

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node == None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))
            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))
            
        s = "Tree\n"

        previous_level = -1

        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s

def pre_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node != None:
            visit_order.append(node.get_value())
            traverse(node.get_left_child())
            traverse(node.get_right_child())
    traverse(root)
    return visit_order

def in_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node != None:
            traverse(node.get_left_child())
            visit_order.append(node.get_value())
            traverse(node.get_right_child())
    traverse(root)
    return visit_order

def post_order(tree):
    visit_order = list()
    root = tree.get_root()

    def traverse(node):
        if node != None:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visit_order.append(node.get_value())
    traverse(root)
    return visit_order


node0 = Node()
print(f"""
    value: {node0.value}
    lseft: {node0.left}
    right: {node0.right}
""")

node1 = Node("apple")
print(f"""
    value: {node1.value}
    lseft: {node1.left}
    right: {node1.right}
""")

node2 = Node("apple1")
node3 = Node("apple2")
node4 = Node("apple3")

node2.set_left_child(node3)
node2.set_right_child(node4)


tree = Tree("apple")
banana = Node('banana')
cherry = Node('cherry')
dates = Node("dates")

node = tree.get_root()
node.set_left_child(banana)
node.set_right_child(cherry)
banana.set_left_child(dates)

# tree.dfs()

t = pre_order(tree)
print(t)
t = in_order(tree)
print(t)
t = post_order(tree)
print(t)


# q  = deque()
# q.appendleft('apple')
# q.appendleft('banana')
# print(q)

class Queue():
    def __init__(self):
        self.q = deque()
    
    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue> here>\n--------------\n"
            s += "\n--------------\n".join([str(item) for item in self.q])
            s += "\n--------------\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)

def bfs(tree):
    # queue
    q = Queue()
    # visit_order
    visit_order = list()
    # start at root
    node = tree.get_root()
    # add root to queue
    q.enq(node)
    # while queue is not empty
    while len(q) > 0:
    # dequeue the node
        node = q.deq()
    # visit that node
        visit_order.append(node)
    # add left child if exists
        if node.has_left_child():
            q.enq(node.get_left_child())
    # add right child if exists
        if node.has_right_child():
            q.enq(node.get_right_child())

    # return the visit order
    return visit_order


print(bfs(tree))
print(tree)

btree = Tree(1)
btree.insert_with_loop(5)
btree.insert_with_loop(6)
btree.insert_with_loop(4)
btree.insert_with_loop(2)
btree.insert_with_loop(5)
# print(btree)

print(btree.search(8))
print(btree.search(2))

brtree = Tree(1)
brtree.insert_with_loop(5)
brtree.insert_with_loop(6)
brtree.insert_with_loop(4)
brtree.insert_with_loop(2)
brtree.insert_with_loop(5)
print(brtree)
brtree.delete(5)
brtree.delete(1)
brtree.delete(4)
print(brtree)