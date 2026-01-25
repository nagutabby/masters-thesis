def calculate_vcs_metrics(stats):
    if stats is None:
        return {
            'num_files': None,
            'lines_added': None,
            'lines_deleted': None,
            'entropy': None
        }

    nf = stats['files_changed']
    la = stats['lines_added']
    ld = stats['lines_deleted']

    entropy = calculate_entropy(stats['lines_per_file'])

    return {
        'num_files': nf,
        'lines_added': la,
        'lines_deleted': ld,
        'entropy': entropy
    }