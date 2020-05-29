import os
import urllib.parse

import gitlab
import utils

private_token = os.environ.get('GITLAB_PRIVATE_TOKEN')
gl = None

def main():
    utils.check_token(private_token)
    print('start deleting gitlab hierarchy')
    global gl
    gl = gitlab.Gitlab('http://localhost', private_token=private_token)
    delete_groups(gl)
    delete_projects(gl)
    

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
            try:
                group.delete()
            except:
                print('Group ' + group.name + ' is already deleted, no need to do it')
            else:
                print('deleted group ' + group.name + ' in GitLab')
    else:
        print('no group to delete')        


if __name__ == '__main__':
    main()
