import structure
import os

def main():
    print(structure.project_structure_alternative)
    folder_path = '/home/master/Dev/folder'

    actual_structure = []
    print('')

    check(folder_path, actual_structure, None)
    print(actual_structure)

    if actual_structure != structure.project_structure_alternative:
        print('Alarm! Achtung!1')
        exit(1)

def check(folder_path, structure, parent): 
    dirs = os.listdir(folder_path)

    for file in dirs:
        full_path = os.path.join(folder_path, file) 
        if os.path.isfile(full_path):
            print(file, 'is file')
        else:
            inner_dirs = os.listdir(full_path)
            not_file = True
            for inner_file in inner_dirs:
                full_inner_path = os.path.join(folder_path, file, inner_file)
                if not os.path.isdir(full_inner_path):
                    not_file = False
                    print(file, 'is project')
                    if parent is None:
                        structure.append({'path': file, 'type': 'project'}) 
                    else:
                        path_with_parent = os.path.join(parent, file)
                        structure.append({'path': path_with_parent, 'type': 'project'})
            if not_file == True and len(inner_dirs) > 0:
                print(file, 'is group')
                if parent is None:
                    structure.append({'path': file, 'type': 'group'}) 
                    check(full_path, structure, file)
                else:
                    path_with_parent = os.path.join(parent, file)
                    structure.append({'path': path_with_parent, 'type': 'group'}) 
                    check(full_path, structure, path_with_parent) 
               
if __name__ == '__main__':
    main()
