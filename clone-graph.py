class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    """DFS"""
    visit = {}
    def cloneGraph(self, node):
        if not node:
            return None
        if self.visit.has_key(node):
            return self.visit[node]
        firstnode = UndirectedGraphNode(node.label)
        self.visit[node] = firstnode
        for i in range(len(node.neighbors)):
            firstnode.neighbors.append(self.cloneGraph(node.neighbors[i]))
        return firstnode


    def cloneGraph_dfs(self,node):
        self.visit = {}
        if not node:
            return None
        if self.visit[node]:
            return self.visit[node]
        firstnode = UndirectedGraphNode(node.label)
        self.visit[node] = firstnode
        for i in range(len(node.neighbors)):
            if not self.visit[node.neighbors[i]]:
                firstnode.neighbors.append(self.cloneGraph_dfs(node.neighbors[i]))
        return firstnode

    def cloneGrpah_iteractive(self,node):
        s = []

        hm = {}
        head = UndirectedGraphNode(node.label)
        hm[node] = head

        s.append(node)
        while len(s) > 0:
            v = s.pop(0)
            for neighbor in v.neighbors:
                if neighbor not in hm:
                    s.append(neighbor)
                    newn = UndirectedGraphNode(neighbor.label)
                    hm[neighbor] = newn
                hm[v].neighbors.extend(neighbor.neighbors[:])
        return head



