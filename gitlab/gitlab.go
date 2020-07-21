package gitlab

import (
	"log"

	"github.com/xanzy/go-gitlab"
)

type Client interface {
	GetProjects() []*gitlab.Project
}

type gitlabConnectedClient struct {
	apiURL             string
	impersonationToken string
}

func ConnectedClient(apiURL, impersonationToken string) *gitlabConnectedClient {
	return &gitlabConnectedClient{
		apiURL:             apiURL,
		impersonationToken: impersonationToken,
	}
}

func (client gitlabConnectedClient) GetProjects() []*gitlab.Project {
	git, err := gitlab.NewClient(client.impersonationToken, gitlab.WithBaseURL(client.apiURL))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	projects, _, err := git.Projects.ListProjects(&gitlab.ListProjectsOptions{})
	if err != nil {
		log.Fatalf("Failed to list gitlab projects: %v", err)
	}

	return projects
}

var (
	// URL holds the address of GitLab server
	URL string
	// Token is impersonation token of user with access to GitLab API
	Token string

	ConnectedGitlabClient *gitlabConnectedClient
)

func GetProjects(ApiURL string, token string) []*gitlab.Project {
	git, err := gitlab.NewClient(token, gitlab.WithBaseURL(ApiURL))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}

	projects, _, err := git.Projects.ListProjects(&gitlab.ListProjectsOptions{})
	if err != nil {
		log.Fatalf("Failed to list gitlab projects: %v", err)
	}

	return projects
}
