package cmd

import (
	"github.com/go-git/go-git/v5"
	"github.com/xanzy/go-gitlab"
	"os"
	"testing"
)

type mockGitLabClient struct {
	projects []*gitlab.Project
}

func (mock mockGitLabClient) GetProjects() []*gitlab.Project {
	return mock.projects
}

type mockGitCloner struct {
	called  bool
	path    string
	options *git.CloneOptions
}

func (mock *mockGitCloner) CloneRepo(path string, repoUrl string) (*git.Repository, error) {
	mock.called = true
	mock.path = path
	mock.options = &git.CloneOptions{
		URL:      repoUrl,
		Progress: os.Stdout,
	}
	repository := git.Repository{}
	return &repository, nil
}

type mockOsManager struct {
	dirExist bool
}

func (mock *mockOsManager) CheckDirExist(path string) bool {
	return mock.dirExist
}

func TestHappyPathCloning(t *testing.T) {
	// given
	cloningPath = "/home"
	project := gitlab.Project{
		Name:         "sample",
		SSHURLToRepo: "sample-url",
	}
	projects := []*gitlab.Project{&project}
	mockClient := mockGitLabClient{
		projects: projects,
	}
	gitCloner := mockGitCloner{
		called:  false,
		path:    "",
		options: nil,
	}
	mockOsManager := mockOsManager{dirExist: true}

	// when
	RunClone(&mockClient, &gitCloner, &mockOsManager)

	// then
	if !gitCloner.called {
		t.Errorf("Did not called git cloner")
	}
	if gitCloner.path != "/home/sample" {
		t.Errorf("Incorrect path passed to cloner!")
	}
	if gitCloner.options.URL != "sample-url" {
		t.Errorf("Incorrect SSH repo url passed to cloner!")
	}

}

func TestEmptyProjects(t *testing.T) {
	// given
	cloningPath = "/home"
	var projects []*gitlab.Project
	mockClient := mockGitLabClient{projects: projects}
	gitCloner := mockGitCloner{
		called:  false,
		path:    "",
		options: nil,
	}
	mockOsManager := mockOsManager{dirExist: true}

	// when
	RunClone(&mockClient, &gitCloner, &mockOsManager)

	// then
	if gitCloner.called {
		t.Errorf("Called but did not want to")
	}
}

func TestDirDoesNotExist(t *testing.T) {
	// given
	cloningPath = "/home"
	var projects []*gitlab.Project
	mockClient := mockGitLabClient{projects: projects}
	gitCloner := mockGitCloner{
		called:  false,
		path:    "",
		options: nil,
	}
	mockOsManager := mockOsManager{dirExist: false}

	// when
	err := RunClone(&mockClient, &gitCloner, &mockOsManager)

	// then
	if err == nil {
		t.Errorf("Error should be thrown because directory does not exist")
	}
}
