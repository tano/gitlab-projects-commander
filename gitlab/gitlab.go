package gitlab

import (
	"log"

	"github.com/xanzy/go-gitlab"
)

var (
	// URL holds the address of GitLab server
	URL string
	// Token is impersonation token of user with access to GitLab API
	Token string
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
