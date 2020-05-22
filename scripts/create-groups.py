import os
import urllib.parse

import requests

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')


def main():
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)
    print('start creating gitlab hierarchy')
    big_a_group_a_id = create_group('big-group-a', 'big-group-a', None)
    create_project('big-group-a-nested-1-project-1', 'big-group-a/big-group-a-nested-1-project-1', big_a_group_a_id)
    big_a_group_a_nested_1_id = create_group('big-group-a-nested-1', 'big-group-a/big-group-a-nested-1',
                                             big_a_group_a_id)
    create_project('big-group-a-nested-1-project-1', 'big-group-a/big-group-a-nested-1/big-group-a-nested-1-project-1',
                   big_a_group_a_nested_1_id)
    create_project('big-group-a-nested-1-project-2', 'big-group-a/big-group-a-nested-1/big-group-a-nested-1-project-2',
                   big_a_group_a_nested_1_id)
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
        print('creating group ' + name)
        creation_request = {'name': name, 'path': url_encoded_path}
        if parent_id is not None:
            creation_request['parent_id'] = parent_id
        create_group_response = requests.post('http://localhost/api/v4/groups', data=creation_request,
                                              headers={'Private-Token': private_token})
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
