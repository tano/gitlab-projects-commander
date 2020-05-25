package gitlab

import (
	"fmt"
	"log"

	"github.com/xanzy/go-gitlab"
)

func GetProjects(ApiURL string, token string) []*gitlab.Project {
	git, err := gitlab.NewClient(token, gitlab.WithBaseURL(ApiURL))
	if err != nil {
		log.Fatalf("Failed to create client: %v", err)
		// return make([]gitLabProject, 0)
	}

	projects, _, err := git.Projects.ListProjects(&gitlab.ListProjectsOptions{})
	if err != nil {
		log.Fatalf("Failed to list gitlab projects: %v", err)
		// return make([]gitLabProject, 0)
	}

	for _, project := range projects {
		fmt.Println("project:", project)
	}

	return projects
}
