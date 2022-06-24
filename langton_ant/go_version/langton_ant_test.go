package main

import (
	"github.com/stretchr/testify/assert"
	"github.com/stretchr/testify/suite"
	"testing"
)

type AntTestSuite struct {
	suite.Suite
	VariableThatShouldStartAtFive int
}

// In order for 'go test' to run this suite, we need to create
// a normal test function and pass our suite to suite.Run
func TestAntTestSuite(t *testing.T) {
	suite.Run(t, new(AntTestSuite))
}

//// Make sure that VariableThatShouldStartAtFive is set to five
//// before each test
//func (s *AntTestSuite) SetupTest() {
//	s.VariableThatShouldStartAtFive = 5
//}

// All methods that begin with "Test" are run as tests within a
// suite.
func (s *AntTestSuite) TestExample() {
	assert.Equal(s.T(), 5, s.VariableThatShouldStartAtFive)
}
