def min_steps_to_uniform(arr: list[int], k: int) -> int:
    arr_len = len(arr)

    if arr_len == 0:
        return 0
    if arr_len == 1:
        return 0
    if arr_len < k:
        return -1
    if all(element == arr[0] for element in arr):
        return 0

    current_state = tuple(arr)
    all_states = {current_state}
    
    steps = 0
    while True:
        steps += 1

        element_to_move = current_state[k - 1]

        next_state = current_state[1:] + (element_to_move,)

        if all(element == next_state[0] for element in next_state):
            return steps

        if next_state in all_states:
            break
            
        all_states.add(next_state)
        current_state = next_state

    return -1

arr = [1, 2, 1, 2]
k = 4
print(min_steps_to_uniform(arr, k))