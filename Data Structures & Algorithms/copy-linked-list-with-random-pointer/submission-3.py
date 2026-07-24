

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        def copy_node(node: Node, nodes: dict) -> Node | None:
            if node is None:
                return None
            new_node = Node(node.val)
            _id = id(node)
            nodes[_id] = nodes.get(_id, new_node)
            return new_node

        # create a copy of all nodes
        nodes = {} 
        cur = head
        while cur is not None:
            copy_node(cur, nodes)
            cur = cur.next
        
        cur = head
        first_node = nodes.get(id(cur), None)
        while cur is not None:
            new_node = nodes[id(cur)]
            new_node.next = nodes[id(cur.next)] if cur.next is not None else None
            new_node.random = nodes[id(cur.random)] if cur.random is not None else None

            cur = cur.next
        return first_node
            