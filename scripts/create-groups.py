import os
import requests

gitlab_hierarchy = {
    'type': 'group',
    'name': 'big-group-a',
    'children': [
        {
            'type': 'group',
            'name': 'big-group-a-nested-1',
            'children': [
                {
                    'type': 'project',
                    'name': 'big-group-a-nested-1-project-1'
                },
                {
                    'type': 'project',
                    'name': 'big-group-a-nested-1-project-2'
                }
            ]
        },
        {
            'type': 'project',
            'name': 'big-group-a-project-1'
        }
    ]
}

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')


def main():
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)
    print('start creating gitlab hierarchy ' + str(gitlab_hierarchy))
    big_a_group_a_id = create_group('big-group-a', 'big-group-a', None)
    create_project('big-group-a-nested-1-project-1', big_a_group_a_id)
    big_a_group_a_nested_1_id = create_group('big-group-a-nested-1', 'big-group-a-nested-1',
                                             big_a_group_a_id)
    create_project('big-group-a-nested-1-project-1', big_a_group_a_nested_1_id)
    create_project('big-group-a-nested-1-project-2', big_a_group_a_nested_1_id)
    print('end creating gitlab hierarchy')


def create_group(name, path, parent_id):
    print('creating group ' + name)
    creation_request = {'name': name, 'path': path}
    if parent_id is not None:
        creation_request['parent_id'] = parent_id
    response = requests.post('http://localhost/api/v4/groups', data=creation_request,
                             headers={'Private-Token': private_token})
    if response.status_code == 201:
        group_id = response.json()['id']
        print('successfully created group ' + name + ' with id ' + str(group_id))
        return group_id
    elif response.status_code == 400:
        response = requests.get('http://localhost/api/v4/groups/' + name,
                                headers={'Private-Token': private_token})
        group_id = response.json()['id']
        print('group ' + name + ' already exist, id is ' + str(group_id))
        return group_id


def create_project(name, group_id):
    print('creating project ' + name)
    response = requests.post('http://localhost/api/v4/groups', data={'name': name, 'namespace_id': group_id},
                             headers={'Private-Token': private_token})
    if response.status_code == 201:
        print('successfully project ' + name)


if __name__ == '__main__':
    main()
