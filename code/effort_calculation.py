def calculate_effort(code_churn, num_files, entropy):
    if num_files == 0 or code_churn == 0:
        raw_effort = 1.0
    elif num_files == 1:
        raw_effort = float(code_churn)
    elif entropy is None or entropy == 0 or np.isnan(entropy):
        raw_effort = float(code_churn)
    else:
        raw_effort = code_churn * (num_files ** entropy)

    effort = np.log(raw_effort + 1)

    return effort