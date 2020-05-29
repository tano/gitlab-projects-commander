package cmd

import (
	"fmt"
	"github.com/spf13/cobra"
	"github.com/tano/gitlab-projects-commander/gitlab"
	"os"
)

var rootCmd = &cobra.Command{
	Use:   "gitlab-projects-commander",
	Short: "gitlab-projects-commander is a tool which helps managing multiple GitLab projects",
	Long: `gitlab-projects-commander is a tool which helps managing multiple GitLab projects.
It now supports cloning hierarchy of all GitLab projects onto local filesystem while keeping the
structure of the proejcts (folders and subfolders).

Example: gitlab-projects-commander clone --gitlab-url https://gitlab.example.com
`,
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}

func init() {
	rootCmd.PersistentFlags().StringVar(&gitlab.URL, "gitlab-url", "http://localhost", "Address of GitLab server (default is http://localhost)")
	rootCmd.PersistentFlags().StringVar(&gitlab.Token, "token", "", "Impersonation token of user with access to GitLab API")
}
