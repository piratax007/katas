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

func (s *kataSuite) Test_cat_countingJump_updatesTheNumberOfJumpsUntilTheCatReachTheFinish() {
	meg := cat{
		start:      1,
		finish:     1,
		distance:   0,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(0, meg.countJumps)

	meg = cat{
		start:      1,
		finish:     2,
		distance:   1,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(1, meg.countJumps)

	meg = cat{
		start:      3,
		finish:     5,
		distance:   2,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(2, meg.countJumps)

	meg = cat{
		start:      2,
		finish:     5,
		distance:   3,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(1, meg.countJumps)

	meg = cat{
		start:      1,
		finish:     6,
		distance:   5,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(3, meg.countJumps)

	meg = cat{
		start:      1,
		finish:     5,
		distance:   4,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(2, meg.countJumps)

	meg = cat{
		start:      1,
		finish:     14,
		distance:   13,
		countJumps: 0,
	}
	meg.countingJumps()
	s.Equal(5, meg.countJumps)
}

func (s *kataSuite) Test_cats_returnsTheNumbersOfJumpsNeededToReachTheFinish() {
	s.Equal(2, cats(1, 5))
}
