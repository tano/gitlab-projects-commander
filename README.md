# gitlab-projects-commander
Project for managing hierarchy of GitLab projects with command-line

![Kotlin/Native CI](https://github.com/tano/gitlab-projects-commander/workflows/Kotlin/Native%20CI/badge.svg)

# Development process
## Local environment setup
### Pre-requirements
* Up-to date Docker is installed on your local machine.
* Python3 is installed on your local machine.
### Preparing local GitLab installation
1. Set GITLAB_HOME environment variable
```export GITLAB_HOME="<YOUR_USER_HOME>/gitlab-home"```
2. Launch GitLab start script (sudo is required!). 
```sudo -E ./start-gitlab.sh```
Next time you'll be able to start/stop your GitLab installation by container name - gitlab 
3. Wait until initialization is finished
```docker logs -f gitlab```
4. Go to localhost with your browser and set new admin password fo your local GitLab installation
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
2. launch "create-groups.sh"
```./create-groups.sh```
## Building
### MacOS
1. Build binary executable
```./gradlew nativeBinaries```
