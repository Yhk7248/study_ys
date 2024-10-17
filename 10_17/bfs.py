from collections import deque

# 트리의 노드 구조 정의
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

# BFS 구현
class TreeBFS:
    def __init__(self, root):
        self.root = root

    def bfs(self):
        visited = set()
        queue = deque([self.root])

        while queue:
            node = queue.popleft()  # 큐에서 노드를 꺼냄
            if node.value not in visited:
                print(node.value)
                visited.add(node.value)

                # 현재 노드의 자식 노드를 큐에 추가
                for child in node.children:
                    if child.value not in visited:
                        queue.append(child)


if __name__ == "__main__":
    root = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)
    child4 = TreeNode(5)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(child3)
    child1.add_child(child4)

    # BFS 실행
    tree_bfs = TreeBFS(root)
    print("BFS:")
    tree_bfs.bfs()
