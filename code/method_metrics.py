def calculate_complexity_changes(complexity_data):
    if len(complexity_data) == 0:
        return {
            'current_commit': None,
            'ccn_change': None,
            'length_change': None,
            'tokens_change': None,
            'operation_type': 'NaN'
        }
    elif len(complexity_data) == 1:
        single_data = complexity_data[0]

        if single_data['commit_order'] == 1:
            return {
                'current_commit': single_data['commit_hash'],
                'ccn_change': None,
                'length_change': None,
                'tokens_change': None,
                'operation_type': 'deleted'
            }
        else:
            return {
                'current_commit': single_data['commit_hash'],
                'ccn_change': None,
                'length_change': None,
                'tokens_change': None,
                'operation_type': 'added'
            }
    elif len(complexity_data) == 2:
        previous_data = complexity_data[0]
        current_data = complexity_data[1]

        ccn_change = current_data['ccn'] - previous_data['ccn']
        length_change = current_data['length'] - previous_data['length']
        tokens_change = current_data['tokens'] - previous_data['tokens']

        return {
            'current_commit': current_data['commit_hash'],
            'ccn_change': ccn_change,
            'length_change': length_change,
            'tokens_change': tokens_change,
            'operation_type': 'modified'
        }
    else:
        return {
            'current_commit': None,
            'ccn_change': None,
            'length_change': None,
            'tokens_change': None,
            'operation_type': 'NaN'
        }