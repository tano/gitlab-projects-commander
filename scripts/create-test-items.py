import os
import urllib.parse

import gitlab

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')
gl = None #todo: remove useless variable

def main():
    check_token()
    print('start creating gitlab hierarchy')
    global gl
    gl = gitlab.Gitlab('http://localhost', private_token=private_token)   
    check_gitlab_is_clean() #check is gitlab empty to avoid corruption of exising data
    faceboak_group = create_group('faceboak')
    instagrum_group = create_group('instagrum', faceboak_group.id)
    create_project('mobile-app',  instagrum_group.id)
    create_project('website',  instagrum_group.id)
    print('end creating gitlab hierarchy')

def check_token():
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)

def check_gitlab_is_clean():
    projects = gl.projects.list()
    groups = gl.groups.list()
    if len(projects) > 0 or len(groups) > 0:
        print('your GitLab is not clean, will create test items only on clean GitLab, please launch delete-test-items.sh')
        exit(1)

def create_group(group_name, parent_project_id = None):
    group_creation_request = {'name': group_name, 'path': group_name}
    if parent_project_id is not None:
        group_creation_request['parent_id'] = parent_project_id
    created_group = gl.groups.create(group_creation_request)
    print('created group ' + created_group.name + ' and id ' + str(created_group.id))
    return created_group

def create_project(project_name, parent_namespace_id):
    project_creation_request = {'name': project_name, 'path': project_name, 'namespace_id': parent_namespace_id}
    created_project = gl.projects.create(project_creation_request)
    print('created project ' + project_name + ' and id ' + str(created_project.id))
    file_creation_request = {'file_path': 'testfile.txt',
                 'branch': 'master',
                 'content': 'this is just a test',
                 'author_email': 'test@example.com',
                 'author_name': 'yourname',
                 'commit_message': 'Create testfile'}
    created_project.files.create(file_creation_request)
    return created_project


if __name__ == '__main__':
    main()
