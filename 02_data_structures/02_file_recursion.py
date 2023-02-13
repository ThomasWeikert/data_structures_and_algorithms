import os

def find_files(suffix, path):
    if not suffix or not path:
        return []

    files = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isfile(full_path) and full_path.endswith(suffix):
            files.append(full_path)
        elif os.path.isdir(full_path):
            files.extend(find_files(suffix, full_path))

    print(files)
    return files

def test_find_files():
    # 1. test case
    suffix = "h"
    path = "./testdir/subdir5"
    assert find_files(suffix, path) == ['./testdir/subdir5/a.h']

    # 2. test case
    suffix = ""
    path = "./testdir/subdir4"
    assert find_files(suffix, path) == []
    
    # 3. test case
    suffix = ".gitkeep"
    path = "./testdir/invalid_dir"
    try:
        result = find_files(suffix, path)
        assert result == []
    except FileNotFoundError as e:
        assert str(e) == "[Errno 2] No such file or directory: './testdir/invalid_dir'"



test_find_files()