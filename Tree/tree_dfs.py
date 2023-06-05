def dfs(root):
    if root is None:
        return
    dfs(root.eft)
    dfs(root.right)


# dfs(root)
