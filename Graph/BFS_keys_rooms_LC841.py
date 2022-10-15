""" There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise."""

from collections import defaultdict
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = self.adjList(rooms)
        visited = set()
        stack = [0]
        
        while stack:
            s = stack.pop()
            visited.add(s)
            for neighbor in  graph[s]:
                if neighbor not in visited:
                    stack.insert(0,neighbor)
        return (len(visited) == len(rooms))
        
    def adjList(self,rooms):
            d= defaultdict(List)
            for i in range(len(rooms)):
                d[i]=rooms[i]
            return d