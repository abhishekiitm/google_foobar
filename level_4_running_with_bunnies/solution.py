
def get_next_state(state, actions, action_idx):
    rescued_bunnies, time_limit, curr_idx = state
    bunny_idx = action_idx-1
    
    next_rescued_bunnies = tuple([rescued_bunnies[i] if i!=bunny_idx else True for i in range(len(rescued_bunnies))])
    next_time_limit = time_limit - actions[action_idx]
    next_action_idx = action_idx

    return (next_rescued_bunnies, next_time_limit, next_action_idx), next_action_idx

def should_terminate(state, min_weight):
    rescued_bunnies, time_limit, curr_idx = state
    if time_limit < min_weight: 
        return True
    return False
    
def get_min_weight(G):
    min_weight = float("inf")
    for row in G:
        for elem in row:
            min_weight = min(min_weight, elem)
    return min_weight

def all_saved(state, bulkhead):
    rescued_bunnies, time_limit, curr_idx = state
    if all(rescued_bunnies) and curr_idx == bulkhead and time_limit > -1:
        return True
    return False

def update_best(state, best, bulkhead):
    rescued_bunnies, time_limit, curr_idx = state
    arr = list(range(100+len(rescued_bunnies), 100, -1))
    if curr_idx == bulkhead and time_limit>-1:
        sum_new = sum([arr[i] if bunny else 0 for i, bunny in enumerate(rescued_bunnies)])
        sum_old = sum([arr[i] if bunny else 0 for i, bunny in enumerate(best)])
        if sum_new > sum_old: best = rescued_bunnies
    return best
    

def solution(times, time_limit):
    l = list(range(len(times)-2))

    visited, stacked = {}, {}

    init_state = (tuple([False for i in range(len(times)-2)]), time_limit, 0)
    init_curr_idx = 0
    init_action_idx = 0

    min_weight = get_min_weight(times)
    best = [0 for i in range(len(times)-2)]
    
    traverse = [(init_state, init_curr_idx, init_action_idx)]
    stacked[init_state] = True
    while traverse:
        state, curr_idx, action_idx = traverse.pop()
        if action_idx == len(times[0]):
            visited[state] = True
            continue

        next_state, next_idx = get_next_state(state, times[curr_idx], action_idx)
        if all_saved(state, len(times[0])-1): return l
        best = update_best(next_state, best, len(times[0])-1)
        if should_terminate(next_state, min_weight):
            visited[next_state] = True
            action_idx += 1
            traverse.append((state, curr_idx, action_idx))
            continue
        action_idx += 1
        traverse.append((state, curr_idx, action_idx))
        if not visited.get(next_state) and not stacked.get(next_state):
            traverse.append((next_state, next_idx, 0))
            stacked[next_state] = True

    i, ret_arr =0, []
    for elem in best:
        if elem: ret_arr.append(i)
        i+=1

    return ret_arr
    
