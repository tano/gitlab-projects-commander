/*
Copyright © 2020 tano <tanoshkin@yandex.ru>
*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// cloneCmd represents the clone command
var cloneCmd = &cobra.Command{
	Use:   "clone",
	Short: "clone allows you to clone recursively hierarchy of GitLab projects",
	Long: `clone allows you to clone recursively hierarchy of GitLab projects. For example:

gitlab-projects-commander clone --gitlab-url https://gitlab.example.com
`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("clone called")
	},
}

func init() {
	rootCmd.AddCommand(cloneCmd)
}
