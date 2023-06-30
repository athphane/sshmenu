import os


def expand_path(path):
    # Check if input path is a user relative path, and expand the path if it is
    if path.startswith("~"):
        path = os.path.expanduser(path)

    return path
