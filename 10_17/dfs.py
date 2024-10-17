"""
1. DFS 알고리즘(깊이 우선 탐색)

    루트 노드(혹은 다른 임의의 노드)에서 시작해서 다음 분기(branch)로 넘어가기 전에
    해당 분기를 완벽하게 탐색하는 방식을 말한다.

2. 예시(미로찾기)

    미로찾기를 할때 최대한 한 방향으로 갈 수 있을 때까지 끝까지 가다가
    더이상 갈 수 없게 되었을 때 다시 가장 가까운 갈림길로 와서
    들어가지 않은 다른 갈림길로 들어가는 경우 "깊이 우선 탐색 방식" 이라고 한다.

3. DFS

    1) 모든 노드를 탐색하고자 하는 경우
    2) 깊이 우선 탐색(DFS)이 너비 우선 탐색(BFS)보다 구현이 간단하다.
    3) 검색 속도는 너비 우선 탐색(BFS) 에 비해서 느리다.
"""


# 트리의 노드 구조 정의
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


# DFS 구현 (재귀적 방식)
def dfs_recursive(node, visited=None):
    if visited is None:
        visited = set()

    # 현재 노드를 방문 표시
    print(node.value)
    visited.add(node.value)

    # 자식 노드를 탐색
    for child in node.children:
        if child.value not in visited:
            dfs_recursive(child, visited)


# DFS 구현 (스택을 이용한 방식)
def dfs_stack(root):
    visited = set()
    stack = [root]

    while stack:
        node = stack.pop()
        if node.value not in visited:
            print(node.value)
            visited.add(node.value)

        # 자식 노드를 스택에 추가 (역순으로 추가해서 처음 자식부터 탐색)
        for child in reversed(node.children):
            if child.value not in visited:
                stack.append(child)


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

    # DFS 실행
    print("DFS (재귀적 방법):")
    dfs_recursive(root)

    print("\nDFS (스택 사용 방법):")
    dfs_stack(root)
