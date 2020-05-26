import os
import urllib.parse

import gitlab

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')


def main():
    if private_token is None:
        print('please set GITLAB_PRIVATE_TOKEN environment variable')
        exit(1)
    print('start deleting gitlab hierarchy')
    gl = gitlab.Gitlab('http://localhost', private_token=private_token)
    delete_projects(gl)
    delete_groups(gl)


def delete_projects(gl):
    projects = gl.projects.list()
    if len(projects) != 0:
        print('deleting projects in GitLab')
        for project in projects:
            print('deleting project ' + project.name + ' in GitLab')
            project.delete()
            print('deleted project ' + project.name + ' in GitLab')
    else:
        print('no projects to delete')        


def delete_groups(gl):
    groups = gl.groups.list()
    if len(groups) != 0:
        print('deleting groups in GitLab')
        for group in groups:
            print('deleting group ' + group.name + ' in GitLab')
            group.delete()
            print('deleted group ' + group.name + ' in GitLab')
    else:
        print('no group to delete')        


if __name__ == '__main__':
    main()
