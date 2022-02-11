import sys
import re
import os
import shutil


def cast_deleter(path_to_project_dir):
    shutil.copytree(path_to_project_dir, f'{path_to_project_dir}_without_typecast')
    list_with_paths_py_files = []
    for root, dirs, files in os.walk(f'{path_to_project_dir}_without_typecast'):
        for file in files:
            if file.endswith(".py"):
                path_file = os.path.join(root, file)
                list_with_paths_py_files.append(path_file)
    for file in list_with_paths_py_files:
        f = open(file, 'r', encoding='utf-8')
        pattern = r"(cast\(.+?,\s|\))"
        code = re.sub(pattern, '', f.read())
        f.close()
        os.remove(file)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(code)


if __name__ == '__main__':
    cast_deleter(sys.argv[1].rstrip('/\/'))
