pre_res = []
in_res = []
post_res = []

def preorder(tree, root):
    pre_res.append(tree)
    if tree[root][0] != '.' or None:
        preorder(tree, tree[root][0])
    if tree[root][1] != '.' or None:
        preorder(tree, tree[root][1])



tree = {}
for _ in range(int(input())):
    r, l, v = input().split()
    tree[r] = [l, v]
print(tree)
preorder(tree, 'A')
print(pre_res)