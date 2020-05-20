# gitlab-projects-commander
Project for managing hierarchy of GitLab projects with command-line

## Local environment setup
### Pre-requirements
1. Up-to date Docker is installed.
## Preparing local GitLab installation
1. Set GITLAB_HOME environment variable
```export GITLAB_HOME="<YOUR_USER_HOME>/gitlab-home"```
2. Launch GitLab start script (sudo is required!)
```sudo -E ./start-gitlab.sh```
3. Wait until initialization is finished
```docker logs -f gitlab```
4. Go to localhost with your browser and set new admin password fo your local GitLab installation
5. Login to GitLab with root/<your password from p.5>
6. Go to "Admin Area" => "Overview" => "Users" and choose "Administrator"
7. Select "Impersonation Tokens"
8. Fill "Name" with "gitlab-projects-commander", leave "Expires At" blank, select all scopes and hit "Create impersonation token"
 
