def get_commit_change_stats(repo_path, commit_hash):
    try:
        repo = Repo(repo_path)
        commit = repo.commit(commit_hash)

        if not commit.parents:
            return None

        parent = commit.parents[0]

        files_changed = 0
        lines_added = 0
        lines_deleted = 0
        total_lines_before = 0
        lines_per_file = []

        diff_index = parent.diff(commit)

        for diff_item in diff_index:
            if diff_item.change_type in ['A', 'M', 'D', 'R']:
                files_changed += 1

            file_lines_changed = 0

            if diff_item.change_type == 'M':
                try:
                    a_content = diff_item.a_blob.data_stream.read().decode('utf-8', errors='ignore')
                    b_content = diff_item.b_blob.data_stream.read().decode('utf-8', errors='ignore')

                    a_lines = a_content.splitlines()
                    b_lines = b_content.splitlines()

                    total_lines_before += len(a_lines)

                    import difflib
                    diff = difflib.unified_diff(a_lines, b_lines, lineterm='')

                    for line in diff:
                        if line.startswith('+') and not line.startswith('+++'):
                            lines_added += 1
                            file_lines_changed += 1
                        elif line.startswith('-') and not line.startswith('---'):
                            lines_deleted += 1
                            file_lines_changed += 1
                except Exception as e:
                    pass

            elif diff_item.change_type == 'A':
                try:
                    b_content = diff_item.b_blob.data_stream.read().decode('utf-8', errors='ignore')
                    b_lines = b_content.splitlines()
                    lines_added += len(b_lines)
                    file_lines_changed += len(b_lines)
                except:
                    pass

            elif diff_item.change_type == 'D':
                try:
                    a_content = diff_item.a_blob.data_stream.read().decode('utf-8', errors='ignore')
                    a_lines = a_content.splitlines()
                    total_lines_before += len(a_lines)
                    lines_deleted += len(a_lines)
                    file_lines_changed += len(a_lines)
                except:
                    pass

            if file_lines_changed > 0:
                lines_per_file.append(file_lines_changed)

        return {
            'files_changed': files_changed,
            'lines_added': lines_added,
            'lines_deleted': lines_deleted,
            'total_lines_before': total_lines_before,
            'lines_per_file': lines_per_file
        }

    except Exception as e:
        return None