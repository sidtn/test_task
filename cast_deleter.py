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
    count_strings = 0
    for file in list_with_paths_py_files:
        f = open(file, 'r', encoding='utf-8')
        pattern = r"cast\(.+?,\s.+\)"
        new_py_file = ''
        for line in f:
            result = re.search(pattern, line)
            if result:
                string_for_replace = result.group(0).split()[-1].strip(')') + '\n'
                new_line = line.replace(result.group(0), string_for_replace)
                new_py_file += new_line
                count_strings += 1
            else:
                new_py_file += line
        f.close()
        os.remove(file)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_py_file)
    print(f'DONE! {count_strings} lines were rewritten')
    print(f'Path to project - {path_to_project_dir}_without_typecast')


if __name__ == '__main__':
    cast_deleter(sys.argv[1].rstrip('/\/'))
