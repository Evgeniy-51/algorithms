class Node():
    def __init__(self, value: int):
        self.value = value
        self.is_black = True
        self.l_child = None
        self.r_child = None


class Tree():
    def __init__(self):
        self.root = None

    def add(self, val: int) -> bool:
        if self.root:
            res = self.add_node(self.root, val)
            self.root = self.rebalnce(self.root)
            self.root.is_black = True
            return res
        else:
            self.root = Node(val)
            return True

    def add_node(self, node: Node, value: int) -> bool:
        if node.value == value:
            return False
        else:
            if node.value > value:
                if node.l_child:
                    res = self.add_node(node.l_child, value)
                    node.l_child = self.rebalnce(node.l_child)
                    return res
                else:
                    node.l_child = Node(value)
                    node.l_child.is_black = False
                    return True
            else:
                if node.r_child:
                    res = self.add_node(node.r_child, value)
                    node.r_child = self.rebalnce(node.r_child)
                    return res
                else:
                    node.r_child = Node(value)
                    node.r_child.is_black = False
                    return True

    def rebalnce(self, node: Node) -> Node:
        res = node
        while True:
            need_reb = False
            if res.r_child and not res.r_child.is_black and (not res.l_child or not res.l_child.is_black):
                need_reb = True
                res = self.right_swap(res)
            if res.l_child and not res.l_child.is_black and res.l_child.l_child and not res.l_child.l_child.is_black:
                need_reb = True
                res = self.left_swap(res)
            if res.l_child and not res.l_child.is_black and res.r_child and not res.r_child.is_black:
                need_reb = True
                self.color_swap(res)
            if not need_reb:
                break
        return res

    def color_swap(self, node: Node):
        node.r_child.is_black = True
        node.l_child.is_black = True
        node.is_black = False

    def left_swap(self, node: Node) -> Node:
        left_node = node.l_child
        btw_node = left_node.r_child
        left_node.r_child = node
        node.l_child = btw_node
        left_node.is_black = node.is_black
        node.is_black = False
        return left_node

    def right_swap(self, node: Node) -> Node:
        right_node = node.r_child
        btw_node = right_node.l_child
        right_node.l_child = node
        node.r_child = btw_node
        right_node.is_black = node.is_black
        node.is_black = False
        return right_node


tree = Tree()
tree.add(5)
tree.add(2)
tree.add(7)
tree.add(9)
tree.add(3)
tree.add(8)
tree.add(1)

