def solve_lights(num_lights, num_buttons, colors, btn_controls):
    
    val_map = {'R': 0, 'G': 1, 'B': 2}
    
  
    light_to_btns = [[] for _ in range(num_lights)]
    for b_idx, lights in enumerate(btn_controls):
        for l_idx in lights:
            light_to_btns[l_idx].append(b_idx)

    adj = [[] for _ in range(num_buttons)]
  
    self_constraints = {} 

    for l_idx, btns in enumerate(light_to_btns):
        current_color = val_map[colors[l_idx]]
        
        needed = (3 - current_color) % 3

        if len(btns) == 0:
            if needed != 0: return "Impossible"
        elif len(btns) == 1:
            u = btns[0]
            if u in self_constraints and self_constraints[u] != needed:
                return "Impossible"
            self_constraints[u] = needed
        elif len(btns) == 2:
            u, v = btns
            
            adj[u].append((v, needed))
            adj[v].append((u, needed))

    
    visited = [False] * num_buttons
    total_presses = 0

    for i in range(num_buttons):
        if not visited[i]:
            component_nodes = []
            q_comp = [i]
            visited[i] = True
            
          
            idx = 0
            while idx < len(q_comp):
                u = q_comp[idx]
                idx += 1
                component_nodes.append(u)
                for v, _ in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q_comp.append(v)

           
            best_local_sum = float('inf')
            possible = False

            for start_val in range(3):
                
                states = {component_nodes[0]: start_val}
                valid = True
                stack = [component_nodes[0]]
               
                while stack:
                    u = stack.pop()
                    val_u = states[u]

                 
                    if u in self_constraints:
                        if val_u != self_constraints[u]:
                            valid = False
                            break
                    
                    
                    for v, req in adj[u]:
                        target_v = (req - val_u) % 3
                        if v in states:
                            if states[v] != target_v:
                                valid = False
                                break
                        else:
                            states[v] = target_v
                            stack.append(v)
                    
                    if not valid: break
                
                
                if valid and len(states) == len(component_nodes):
                    current_sum = sum(states.values())
                    if current_sum < best_local_sum:
                        best_local_sum = current_sum
                        possible = True

            if not possible:
                return "Impossible"
            total_presses += best_local_sum

    return total_presses



if __name__ == "__main__":
  
    
    L = 3
    B = 3
    S = "RGB"
    
    conns = [[0, 1], [1, 2], [2, 0]]

    res = solve_lights(L, B, S, conns)
    print(f"Pulsaciones mínimas: {res}")