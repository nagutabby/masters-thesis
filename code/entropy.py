def calculate_entropy(lines_per_file):
    if not lines_per_file or len(lines_per_file) == 0:
        return None

    if len(lines_per_file) == 1:
        return 0.0

    total_lines = sum(lines_per_file)
    if total_lines == 0:
        return None

    entropy = 0.0
    for lines in lines_per_file:
        if lines > 0:
            pk = lines / total_lines
            entropy -= pk * np.log2(pk)

    normalized_entropy = entropy / np.log2(len(lines_per_file))
    return normalized_entropy