import sys


input_texto = 


def main():

    input_data = input_texto.split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        
        n = int(next(iterator))
        m = int(next(iterator))
        
        
        A = [next(iterator) for _ in range(n)]
        
        
        B = [next(iterator) for _ in range(n)]
        
       
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            
            adj[u].append(v)
            adj[v].append(u)
            
    except StopIteration:
        return

    vis = [False] * n
    
   
    def get_component(u, nodes):
        vis[u] = True
        nodes.append(u)
        for v in adj[u]:
            if not vis[v]:
                get_component(v, nodes)


    for i in range(n):
        if not vis[i]:
            nodes = []
            get_component(i, nodes)
            
            
            edges = 0
            for u in nodes:
                edges += len(adj[u])
            edges //= 2
            
            
            if edges < len(nodes):
                for u in nodes:
                    if A[u] != B[u]:
                        print("impossible")
                        return
            
           
            else:
                list1 = [A[u] for u in nodes]
                list2 = [B[u] for u in nodes]
                list1.sort()
                list2.sort()
                
                if list1 != list2:
                    print("impossible")
                    return

    print("possible")