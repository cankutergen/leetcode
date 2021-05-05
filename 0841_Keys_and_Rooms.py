class Solution(object):
    def canVisitAllRooms(self, rooms):
        visited = set()        
        visited.add(0)
        
        stack = []
        stack.append(0)
        
        while len(stack) > 0:
            room_index = stack.pop()
            keys = rooms[room_index]
            
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                    
        return len(visited) == len(rooms)
                
        
