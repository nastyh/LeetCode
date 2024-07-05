# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips_bfs(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        """
        O((max(w, h))^2) both where w and h are dimensions of the sea
        partition by quadrants and keep adding to queue while conditions are met
        """
        stack = [(topRight, bottomLeft)]
        count = 0
        while stack:
            tr, bl = stack.pop(0) # taking out top right and bottom left
            if tr.x < bl.x or tr.y < bl.y:
                continue
            if not sea.hasShips(tr, bl):
                continue
            if tr.x == bl.x and tr.y == bl.y: # the only case we want 
                count += 1
                continue
            # midX = (tr.x + bl.x) >> 1 # (tr.x + bl.x) / by 2^1
            # midY = (tr.y + bl.y) >> 1 # (tr.y + bl.y) / by 2^1 
            # we can rewrite these two lines normally
            midX = (tr.x + bl.x) // 2 # (tr.x + bl.x) / by 2^1
            midY = (tr.y + bl.y) // 2 # (tr.y + bl.y) / by 2^1 
            stack.append((Point(midX, tr.y), Point(bl.x, midY + 1)))  # Top-left quadrant
            stack.append((tr, Point(midX + 1, midY + 1)))             # Top-right quadrant
            stack.append((Point(midX, midY), bl))                      # Bottom-left quadrant
            stack.append((Point(tr.x, midY), Point(midX + 1, bl.y)))   # Bottom-right quadrant
        return count
        
    def countShips_division(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
         #Base cases
        if bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            if sea.hasShips(topRight,bottomLeft): return 1
            else: return 0

        # if ships in area divide area
        if sea.hasShips(topRight, bottomLeft):
            #divide vertically
            if topRight.x == bottomLeft.x:
                mid = math.floor((topRight.y+bottomLeft.y)/2)
                return self.countShips(sea, topRight, Point(topRight.x, mid+1)) + self.countShips(sea, Point(topRight.x, mid), bottomLeft)
            #divide horrizontally
            mid = math.floor((topRight.x+bottomLeft.x)/2)
            return self.countShips(sea, Point(mid, topRight.y), bottomLeft) + self.countShips(sea, topRight, Point(mid+1, bottomLeft.y))
        else: return 0