package main

import (
	"testing"

	"github.com/stretchr/testify/suite"
)

type kataSuite struct {
	suite.Suite
	tdir string
}

func TestSuite(t *testing.T) {
	suite.Run(t, new(kataSuite))
}

func (s *kataSuite) SetupTest() {
	s.tdir = s.T().TempDir()
}

func (s *kataSuite) Test_dummy_returnsThree() {
	s.Equal(3, dummy())
}
