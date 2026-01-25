def knapsack_greedy(weights, values, capacity):
    n = len(weights)

    items = []
    for i in range(n):
        if weights[i] > 0:
            ratio = values[i] / weights[i]
            items.append((i, ratio, weights[i], values[i]))
        else:
            items.append((i, 0, weights[i], values[i]))

    items.sort(key=lambda x: x[1], reverse=True)

    selected_indices = []
    total_weight = 0.0
    total_value = 0.0

    for idx, ratio, weight, value in items:
        if total_weight + weight <= capacity:
            selected_indices.append(idx)
            total_weight += weight
            total_value += value

    selected_indices.sort()

    return selected_indices, total_value, total_weight