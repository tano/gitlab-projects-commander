import structure
import os

def main():
    print(structure.project_structure)
    folder_path = '/home/master/Dev/folder'

    actual_structure = {}

    check(folder_path)

def check(folder_path):    
    dirs = os.listdir(folder_path)
    for file in dirs:
        if os.path.isdir(file):
            print(file, ' is file')
        else:
            print(file, ' is directory')
            inner_path = os.path.join(folder_path, file) 
            inner_dirs = os.listdir(inner_path)
            group = True
            for inner_file in inner_dirs:
                if os.path.isfile(inner_file):
                    print(inner_file, 'is project')
                else:
                    print(inner_file, 'is group')

if __name__ == '__main__':
    main()
