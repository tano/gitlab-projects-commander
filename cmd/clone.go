/*
Copyright © 2020 tano <tanoshkin@yandex.ru>
*/
package cmd

import (
	"fmt"
	"log"
	"os"

	"github.com/go-git/go-git/v5"
	"github.com/spf13/cobra"
	"github.com/tano/gitlab-projects-commander/gitlab"
)

// cloneCmd represents the clone command
var cloneCmd = &cobra.Command{
	Use:   "clone",
	Short: "clone allows you to clone recursively hierarchy of GitLab projects",
	Long: `clone allows you to clone recursively hierarchy of GitLab projects. For example:

gitlab-projects-commander clone --gitlab-url https://gitlab.example.com
`,
	Run: func(cmd *cobra.Command, args []string) {
		s := fmt.Sprintf("clone called, GitLab URL is %s and token is %s", GitLabURL, Token)
		fmt.Println(s)
		projects := gitlab.GetProjects(GitLabURL, Token)
		for _, project := range projects {
			effPath := PathForProjects + "/" + project.Name
			m := fmt.Sprintf("going to clone project %s to %s", project.SSHURLToRepo, effPath)
			fmt.Println(m)
			_, err := git.PlainClone(effPath, false, &git.CloneOptions{
				URL:      project.SSHURLToRepo,
				Progress: os.Stdout,
			})
			if err != nil {
				log.Fatalf("Failed to clone repot: %v", err)
				// return make([]gitLabProject, 0)
			}
		}
	},
}

func init() {
	rootCmd.AddCommand(cloneCmd)
}
