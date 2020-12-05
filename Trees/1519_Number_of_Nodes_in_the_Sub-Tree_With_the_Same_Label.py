from collections import defaultdict
def countSubTrees(n, edges, labels):
    g = defaultdict(list)
    for u, v in edges:
        g[u].append(v)
        g[v].append(u)
    ans = {}    
    def dfs(u, parent):
        c = Counter([labels[u]])
        if u in g:
            for v in g[u]:
                if v != parent:
                    c += dfs(v, u)
        ans[u] = c[labels[u]]
        return c             
    dfs(0, 0) 
    return [ans[u] for u in range(n)] 