package gitlab

import (
	"log"

	"github.com/xanzy/go-gitlab"
)

type Client interface {
	GetProjects() []*gitlab.Project
}

type gitlabConnectedClient struct {
	clientInstance *gitlab.Client
}

func ConnectedClient(apiURL, impersonationToken string) *gitlabConnectedClient {
	client, err := gitlab.NewClient(impersonationToken, gitlab.WithBaseURL(apiURL))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
	}
	return &gitlabConnectedClient{
		clientInstance: client,
	}
}

func (client gitlabConnectedClient) GetProjects() []*gitlab.Project {
	projects, _, err := client.clientInstance.Projects.ListProjects(&gitlab.ListProjectsOptions{})
	if err != nil {
		log.Fatalf("Failed to list gitlab projects: %v", err)
	}

	return projects
}

var (
	ConnectedGitlabClient *gitlabConnectedClient
)
