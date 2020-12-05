package rgit

import (
	"github.com/go-git/go-git/v5"
	"os"
)

type GitCloner interface {
	CloneRepo(path string, repoUrl string) (*git.Repository, error)
}

type SimpleGitCloner struct{}

func (cloner SimpleGitCloner) CloneRepo(path string, repoUrl string) (*git.Repository, error) {
	return git.PlainClone(path, false, &git.CloneOptions{
		URL:      repoUrl,
		Progress: os.Stdout,
	})
}
