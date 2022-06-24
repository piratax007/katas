package main

import (
	"github.com/stretchr/testify/mock"
	"github.com/stretchr/testify/suite"
	"testing"
)

package main

import (
"github.com/stretchr/testify/mock"
"testing"

"github.com/stretchr/testify/suite"
)

type simpleSuite struct {
	suite.Suite
}

func TestSuite(t *testing.T) {
	suite.Run(t, new(simpleSuite))
}