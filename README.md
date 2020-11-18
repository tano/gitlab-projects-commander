# gitlab-projects-commander
Project for managing hierarchy of GitLab projects with command-line

# Development process
## Local environment setup
### Pre-requirements
All this software should be installed on your local machine:
* Docker desktop
* Python3 
* Golang 1.14+
### Preparing local GitLab installation
1. Set GITLAB_HOME environment variable
```export GITLAB_HOME="<YOUR_USER_HOME>/gitlab-home"```
2. Launch GitLab start script (sudo is required!). 
```sudo -E ./start-gitlab.sh```
Next time you'll be able to start/stop your GitLab installation by container name - gitlab 
3. Wait until initialization is finished
```docker logs -f gitlab```
4. Go to localhost with your browser and set new admin password for your local GitLab installation
5. Login to GitLab with root/<your password from p.5>
6. Go to "Admin Area" => "Overview" => "Users" and choose "Administrator"
7. Select "Impersonation Tokens"
8. Fill "Name" with "gitlab-projects-commander", leave "Expires At" blank, select all scopes and hit "Create impersonation token"
9. The following request 
```
curl --header "Private-Token: <your_access_token>" http://localhost/api/v4/projects --insecure
```
should give you no authentication error but empty list of projects.
### Creating test data in your GitLab test installation
1. Set GITLAB_PRIVATE_TOKEN environment variable
```export GITLAB_PRIVATE_TOKEN=<your_access_token>```
2. launch "create-groups.sh" in case you want to populate GitLab with some test projects and groups
```./create-groups.sh```
launch "delete-test-items.sh" in case you want to clean up test projects and groups
 GitLab ```./delete-test-items.sh```
3. TODO: add some test data like README to repo (now manually).
## Building
### MacOS
1. Build binary executable
```./gradlew nativeBinaries```
### Checking cloning
1. Add gitlab.example.com host to /etc/hosts as localhost (on Mac).
```sudo vim /etc/hosts```
add ```127.0.0.1 gitlab.example.com``` at the end
2. Add your SSH keys to locally running GitLab instance.
3. Add gitlab.example.com to known_hosts on your machine.