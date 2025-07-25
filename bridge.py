from collections import deque

people_times = {
    'Amogh': 5,
    'Ameya': 10,
    'Grandma': 20,
    'Grandpa': 25
}

# Initial state: All on left
initial_state = (frozenset(people_times.keys()), frozenset(), 'left', 0)

def get_possible_moves(state):
    left, right, pos, time_spent = state
    moves = []
    
    if pos == 'left':
        # Two people cross to the right
        for p1 in left:
            for p2 in left:
                if p1 >= p2:  # avoid duplicates
                    new_left = left - {p1, p2}
                    new_right = right | {p1, p2}
                    time = max(people_times[p1], people_times[p2])
                    moves.append((new_left, new_right, 'right', time_spent + time))
    else:
        # One person returns with umbrella
        for p in right:
            new_left = left | {p}
            new_right = right - {p}
            time = people_times[p]
            moves.append((new_left, new_right, 'left', time_spent + time))
    
    return moves

def bfs_bridge():
    visited = set()
    queue = deque()
    queue.append((initial_state, [initial_state]))
    
    while queue:
        current, path = queue.popleft()
        left, right, pos, time_spent = current
        
        if len(left) == 0 and time_spent <= 60:
            return path
        
        state_id = (left, pos, time_spent)
        if state_id in visited or time_spent > 60:
            continue
        
        visited.add(state_id)
        
        for new_state in get_possible_moves(current):
            queue.append((new_state, path + [new_state]))
    
    return None

# Run BFS
solution = bfs_bridge()

# Display path
print("Bridge Crossing BFS Solution (Steps):\n")
for i, step in enumerate(solution):
    left, right, pos, time = step
    print(f"Step {i}:")
    print(f"  Left : {sorted(left)}")
    print(f"  Right: {sorted(right)}")
    print(f"  Umbrella at: {pos}")
    print(f"  Time used so far: {time} min\n")

# Final time
print(f"Total Time: {solution[-1][3]} minutes")