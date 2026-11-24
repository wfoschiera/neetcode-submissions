from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        tickets.sort()
        for src, dest in tickets[::-1]:
            adj[src].append(dest)

        curr_path = ["JFK"]
        circuit = []

        while len(curr_path) > 0:
            curr_node = curr_path[-1]
            if len(adj[curr_node]) > 0:
                curr_path.append(adj[curr_node].pop())
            else:
                circuit.append(curr_path.pop())

        return circuit[::-1]

