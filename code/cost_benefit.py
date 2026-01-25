def calculate_cost_benefit_greedy(y_true, y_pred_proba, efforts, capacity_ratios):
    total_effort = np.sum(efforts)
    total_bugs = np.sum(y_true)

    results = []

    results.append({
        'capacity_ratio': 0.0,
        'effort_used': 0.0,
        'commits_reviewed': 0,
        'bugs_found': 0.0,
        'review_effort_ratio': 0.0,
        'bug_detection_ratio': 0.0
    })

    for capacity_ratio in capacity_ratios:
        capacity = total_effort * capacity_ratio

        selected_indices, total_value, total_weight = knapsack_greedy(
            weights=efforts,
            values=y_pred_proba,
            capacity=capacity
        )

        bugs_found = np.sum(y_true[selected_indices])

        results.append({
            'capacity_ratio': capacity_ratio,
            'effort_used': total_weight,
            'commits_reviewed': len(selected_indices),
            'bugs_found': bugs_found,
            'review_effort_ratio': total_weight / total_effort if total_effort > 0 else 0,
            'bug_detection_ratio': bugs_found / total_bugs if total_bugs > 0 else 0
        })

    return pd.DataFrame(results)