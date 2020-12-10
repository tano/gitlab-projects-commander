package os

import "os"

type Manager interface {
	CheckDirExist(path string) bool
}

type FsManager struct{}

func (FsManager) CheckDirExist(path string) bool {
	if _, err := os.Stat(path); os.IsNotExist(err) {
		return false
	} else {
		return true
	}
}
