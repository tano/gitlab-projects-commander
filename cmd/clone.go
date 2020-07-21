package cmd

import (
	"fmt"
	"log"
	"os"

	"github.com/go-git/go-git/v5"
	"github.com/spf13/cobra"
	"github.com/tano/gitlab-projects-commander/gitlab"
)

var cloningPath string

func CloneCommand(gl gitlab.Client) *cobra.Command {
	return &cobra.Command{
		Use:   "clone",
		Short: "clone allows you to clone recursively hierarchy of GitLab projects",
		Long: `clone allows you to clone recursively hierarchy of GitLab projects. For example:

gitlab-projects-commander clone --gitlab-url https://gitlab.example.com
`,
		Run: func(cmd *cobra.Command, args []string) {
			s := fmt.Sprintf("clone called, GitLab URL is %s and token is %s", gitlab.URL, gitlab.Token)
			fmt.Println(s)
			// TODO: check if dir is empty or not
			projects := gl.GetProjects()
			for _, project := range projects {
				effPath := cloningPath + "/" + project.Name
				m := fmt.Sprintf("going to clone project %s to %s", project.SSHURLToRepo, effPath)
				fmt.Println(m)
				_, err := git.PlainClone(effPath, false, &git.CloneOptions{
					URL:      project.SSHURLToRepo,
					Progress: os.Stdout,
				})
				if err != nil {
					log.Fatalf("Failed to clone repo: %v", err)
				}
			}
		},
	}
}

func init() {
	rootCmd.AddCommand(CloneCommand(gitlab.ConnectedGitlabClient))
	rootCmd.PersistentFlags().StringVar(&cloningPath, "path", "defaultPath", "Target path to clone GitLab hierarchy")
}
