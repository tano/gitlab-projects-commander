import os
import urllib.parse

import gitlab

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')

def main():
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)
    print('start creating gitlab hierarchy')
    gl = gitlab.Gitlab('http://localhost', private_token=private_token)
    
    projects = gl.projects.list()
    groups = gl.groups.list()
    if len(projects) > 0 or len(groups) > 0:
        print('your GitLab is not clean, will create test items only on clean GitLab, please launch delete-test-items.sh')
        exit(1)
    faceboak_group = gl.groups.create({'name': 'faceboak', 'path': 'faceboak'})
    print('created group ' + faceboak_group.name + ' and id ' + str(faceboak_group.id))
    instagrum_group = gl.groups.create({'name': 'instagrum', 'path': 'instagrum', 'parent_id': faceboak_group.id})
    print('created group ' + instagrum_group.name + ' and id ' + str(instagrum_group.id))
    instagrum_mobile_app = gl.projects.create({'name': 'mobile-app', 'path': 'mobile-app', 'namespace_id': instagrum_group.id})
    print('created project ' + instagrum_mobile_app.name + ' and id ' + str(instagrum_mobile_app.id))
    # projects = gl.projects.list()
    # for project in projects:
    #     print(project)
    # big_a_group_a_id = create_group('big-group-a', 'big-group-a', None)
    # create_project('big-group-a-nested-1-project-1', 'big-group-a/big-group-a-nested-1-project-1', big_a_group_a_id)
    # big_a_group_a_nested_1_id = create_group('big-group-a-nested-1', 'big-group-a-nested-1',
    #                                          big_a_group_a_id)
    # create_project('big-group-a-nested-1-project-1', 'big-group-a-nested-1-project-1',
    #                big_a_group_a_nested_1_id)
    # create_project('big-group-a-nested-1-project-2', 'big-group-a-nested-1-project-2',
    #                big_a_group_a_nested_1_id)
    print('end creating gitlab hierarchy')


def create_group(name, path, parent_id):
    url_encoded_path = urllib.parse.quote_plus(path)
    get_group_response = requests.get('http://localhost/api/v4/groups/' + url_encoded_path,
                                      headers={'Private-Token': private_token})
    if get_group_response.status_code == 200:
        group_id = get_group_response.json()['id']
        print('group ' + name + ' already exist, id is ' + str(group_id))
        return group_id
    elif get_group_response.status_code == 404:
        creation_request = {'name': name, 'path': url_encoded_path}
        print('creating group ' + name + ', and path ' + url_encoded_path)
        if parent_id is not None:
            creation_request['parent_id'] = parent_id
        create_group_response = requests.post('http://localhost/api/v4/groups', data=creation_request,
                                              headers={'Private-Token': private_token})
        print('create group response ' + str(create_group_response.json()))
        group_id = create_group_response.json()['id']
        print('successfully created group ' + name + ' with id ' + str(group_id))
        return group_id


def create_project(name, path, group_id):
    url_encoded_path = urllib.parse.quote_plus(path)
    get_project_response = requests.get('http://localhost/api/v4/projects/' + url_encoded_path,
                                        headers={'Private-Token': private_token})
    if get_project_response.status_code == 200:
        project_id = get_project_response.json()['id']
        print('project ' + name + ' already exist, id is ' + str(project_id))
        return
    elif get_project_response.status_code == 404:
        print('creating project ' + name)
        response = requests.post('http://localhost/api/v4/projects',
                                 data={'name': name, 'namespace_id': group_id},
                                 headers={'Private-Token': private_token})
        if response.status_code == 201:
            print('successfully project ' + name)


if __name__ == '__main__':
    main()
