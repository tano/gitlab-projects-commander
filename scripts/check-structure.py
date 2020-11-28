import structure
import os

def main():
    print(structure.project_structure)
    folder_path = '/home/master/Dev/folder'

    actual_structure = {}
    print('')

    check(folder_path)

def check(folder_path): 
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
            if not_file == True and len(inner_dirs) > 0:
                print(file, 'is group')
                check(full_path)
               
if __name__ == '__main__':
    main()
