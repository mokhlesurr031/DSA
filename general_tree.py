class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            print(child.data)
            


def build_product_tree():
    root = TreeNode('Electronics')

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))


    root.add_child(laptop)
    root.add_child(cellphone)
    return root



root = build_product_tree()
#
# print(root.data)
# print(root.children)
# print(root.children[0].children)
# print(root.parent)

root.print_tree()