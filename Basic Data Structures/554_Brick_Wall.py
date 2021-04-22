from collections import defaultdict
def leastBricks(wall):
    """
    layers define the number of layers in the brick wall.
    width defines the width of each layer. Note that each
    layer has the same width.
    Build a dictionary:
    - d maps each edge location to its frequency
      over the entire wall.
    - edges are numbered from 0 to width. For example, a brick of length 2 at the start of a layer will have
        edges at 0 and 2.
    - Only edges between adjacent bricks are included in d.
    """
    layers = len(wall)
    width = sum(wall[0])
    d = defaultdict(int)
    for layer in wall:
        sum_bricks = 0
        for brick in layer:
            sum_bricks += brick
            if sum_bricks < width:
                d[sum_bricks] += 1
    max_edges = d
    for hash in brick_hash:
        max_edges = max(max_edges, d[hash])
    return layers - max_edges
