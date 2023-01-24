preorder = []
def treeTraversal(inorder, postorder):
	if len(inorder) == 1:
		preorder.append(postorder.pop())
		return
	elif len(inorder) == 0:
		return

	preorder.append(postorder[-1])
	criteria = postorder.pop()
	
	left = inorder[:inorder.index(criteria)]
	right = inorder[inorder.index(criteria)+1:]
	treeTraversal(left, postorder[:len(left)])
	treeTraversal(right, postorder[len(left):])

input()
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
treeTraversal(inorder, postorder)
print(*preorder)