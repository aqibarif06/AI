from collections import deque

# Function to generate all valid next moves
def get_possible_moves(state):
    moves = []
    state = list(state)
    for i in range(len(state)):
        if state[i] == 'W':
            # Move left by 1
            if i - 1 >= 0 and state[i - 1] == '_':
                new_state = state[:]
                new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
                moves.append(''.join(new_state))
            # Jump left over one 'E'
            if i - 2 >= 0 and state[i - 2] == '_' and state[i - 1] == 'E':
                new_state = state[:]
                new_state[i], new_state[i - 2] = new_state[i - 2], new_state[i]
                moves.append(''.join(new_state))
        elif state[i] == 'E':
            # Move right by 1
            if i + 1 < len(state) and state[i + 1] == '_':
                new_state = state[:]
                new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
                moves.append(''.join(new_state))
            # Jump right over one 'W'
            if i + 2 < len(state) and state[i + 2] == '_' and state[i + 1] == 'W':
                new_state = state[:]
                new_state[i], new_state[i + 2] = new_state[i + 2], new_state[i]
                moves.append(''.join(new_state))
    return moves

# BFS Implementation
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque()
    queue.append((initial_state, [initial_state]))
    
    while queue:
        current, path = queue.popleft()
        if current == goal_state:
            return path
        if current in visited:
            continue
        visited.add(current)
        for next_state in get_possible_moves(current):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None

# DFS Implementation
def dfs(initial_state, goal_state):
    visited = set()
    stack = [(initial_state, [initial_state])]
    
    while stack:
        current, path = stack.pop()
        if current == goal_state:
            return path
        if current in visited:
            continue
        visited.add(current)
        for next_state in get_possible_moves(current):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))
    return None

# Run both algorithms and print results
if __name__ == "__main__":
    initial = 'WWW_EEE'
    goal = 'EEE_WWW'

    print("=== BFS Solution ===")
    bfs_path = bfs(initial, goal)
    if bfs_path:
        for i, state in enumerate(bfs_path):
            print(f"Step {i}: {state}")
        print(f"Total steps: {len(bfs_path)-1}")
    else:
        print("No solution found using BFS.")

    print("\n=== DFS Solution ===")
    dfs_path = dfs(initial, goal)
    if dfs_path:
        for i, state in enumerate(dfs_path):
            print(f"Step {i}: {state}")
        print(f"Total steps: {len(dfs_path)-1}")
    else:
        print("No solution found using DFS.")