package main

import (
	"github.com/stretchr/testify/suite"
	"testing"
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

func (s *kataSuite) Test_isFlush_returnsTrueIfTheGivenHandIsFlush() {
	input := hand{
		[]int{},
		[]suit{"H", "D", "S", "C", "D"},
		"",
		0,
	}
	s.False(isFlush(&input))

	input = hand{
		[]int{},
		[]suit{"H", "H", "S", "H", "H"},
		"",
		0,
	}
	s.False(isFlush(&input))

	input = hand{
		[]int{},
		[]suit{"C", "C", "C", "C", "H"},
		"",
		0,
	}
	s.False(isFlush(&input))

	input = hand{
		[]int{},
		[]suit{"D", "C", "C", "C", "H"},
		"",
		0,
	}
	s.False(isFlush(&input))

	input = hand{
		[]int{2, 4, 7, 9, 13},
		[]suit{"C", "C", "C", "C", "C"},
		"",
		0,
	}
	s.True(isFlush(&input))
	s.Equal("flush", input.order)
	s.Equal(13, input.rank)

	input = hand{
		[]int{3, 5, 7, 9, 11},
		[]suit{"S", "S", "S", "S", "S"},
		"",
		0,
	}
	s.True(isFlush(&input))
	s.Equal("flush", input.order)
	s.Equal(11, input.rank)
}

func (s *kataSuite) Test_isStraight_returnsTrueIfTheGivenHandIsStraight() {
	input := hand{
		[]int{2, 3, 5, 9, 13},
		[]suit{},
		"",
		0,
	}
	s.False(isStraight(&input))

	input = hand{
		[]int{2, 3, 4, 5, 8},
		[]suit{},
		"",
		0,
	}
	s.False(isStraight(&input))

	input = hand{
		[]int{2, 3, 4, 5, 6},
		[]suit{},
		"",
		0,
	}
	s.True(isStraight(&input))
	s.Equal("straight", input.order)
	s.Equal(6, input.rank)

	input = hand{
		[]int{10, 11, 12, 13, 14},
		[]suit{},
		"",
		0,
	}
	s.True(isStraight(&input))
	s.Equal("straight", input.order)
	s.Equal(14, input.rank)

	input = hand{
		[]int{5, 6, 7, 8, 9},
		[]suit{},
		"",
		0,
	}
	s.True(isStraight(&input))
	s.Equal("straight", input.order)
	s.Equal(9, input.rank)

	input = hand{
		[]int{2, 3, 4, 5, 14},
		[]suit{},
		"",
		0,
	}
	s.True(isStraight(&input))
	s.Equal("straight", input.order)
	s.Equal(5, input.rank)
}

func (s *kataSuite) Test_isStraightFlush_returnsTrueIfTheGivenHandIsStraightFlush() {
	input := hand{
		[]int{2, 3, 5, 9, 13},
		[]suit{"D", "C", "C", "C", "H"},
		"",
		0,
	}
	s.False(isStraightFlush(&input))

	input = hand{
		[]int{5, 6, 7, 8, 9},
		[]suit{"D", "C", "C", "C", "H"},
		"",
		0,
	}
	s.False(isStraightFlush(&input))

	input = hand{
		[]int{2, 3, 5, 9, 13},
		[]suit{"D", "D", "D", "D", "D"},
		"",
		0,
	}
	s.False(isStraightFlush(&input))

	input = hand{
		[]int{6, 7, 8, 9, 10},
		[]suit{"H", "H", "H", "H", "H"},
		"",
		0,
	}
	s.True(isStraightFlush(&input))
	s.Equal("straight flush", input.order)
	s.Equal(10, input.rank)

	input = hand{
		[]int{2, 3, 4, 5, 14},
		[]suit{"S", "S", "S", "S", "S"},
		"",
		0,
	}
	s.True(isStraightFlush(&input))
	s.Equal("straight flush", input.order)
	s.Equal(5, input.rank)
}

func (s *kataSuite) Test_hasFourOfAKind_returnsTrueIfTheGivenHandHasFourCardsWithTheSameValue() {
	input := hand{
		[]int{8, 9, 10, 11, 12},
		[]suit{},
		"",
		0,
	}
	s.False(hasFourOfAKind(&input))

	input = hand{
		[]int{2, 2, 2, 12, 14},
		[]suit{},
		"",
		0,
	}
	s.False(hasFourOfAKind(&input))

	input = hand{
		[]int{2, 5, 5, 5, 11},
		[]suit{},
		"",
		0,
	}
	s.False(hasFourOfAKind(&input))

	input = hand{
		[]int{2, 2, 2, 2, 13},
		[]suit{},
		"",
		0,
	}
	s.True(hasFourOfAKind(&input))
	s.Equal("four of a kind", input.order)
	s.Equal(2, input.rank)

	input = hand{
		[]int{3, 14, 14, 14, 14},
		[]suit{},
		"",
		0,
	}
	s.True(hasFourOfAKind(&input))
	s.Equal("four of a kind", input.order)
	s.Equal(14, input.rank)
}

func (s *kataSuite) Test_isFullHouse_returnsTrueIfTheGivenHandHasThreeCardOfTheSameValueAndAPair() {
	input := hand{
		[]int{8, 9, 10, 11, 12},
		[]suit{},
		"",
		0,
	}
	s.False(isFullHouse(&input))

	input = hand{
		[]int{2, 5, 5, 5, 11},
		[]suit{},
		"",
		0,
	}
	s.False(isFullHouse(&input))

	input = hand{
		[]int{2, 2, 5, 5, 11},
		[]suit{},
		"",
		0,
	}
	s.False(isFullHouse(&input))

	input = hand{
		[]int{2, 2, 2, 2, 13},
		[]suit{},
		"",
		0,
	}
	s.False(isFullHouse(&input))

	input = hand{
		[]int{3, 14, 14, 14, 14},
		[]suit{},
		"",
		0,
	}
	s.False(isFullHouse(&input))

	input = hand{
		[]int{3, 3, 14, 14, 14},
		[]suit{},
		"",
		0,
	}
	s.True(isFullHouse(&input))
	s.Equal("full house", input.order)
	s.Equal(14, input.rank)

	input = hand{
		[]int{3, 3, 3, 14, 14},
		[]suit{},
		"",
		0,
	}
	s.True(isFullHouse(&input))
	s.Equal("full house", input.order)
	s.Equal(3, input.rank)
}

func (s *kataSuite) Test_hasThreeOfAKind_returnsTrueIfTheGivenHandHasThreeCardOfTheSameValue() {
	input := hand{
		[]int{2, 3, 3, 11, 14},
		[]suit{},
		"",
		0,
	}
	s.False(hasThreeOfAKind(&input))

	input = hand{
		[]int{2, 3, 4, 4, 14},
		[]suit{},
		"",
		0,
	}
	s.False(hasThreeOfAKind(&input))

	input = hand{
		[]int{2, 2, 2, 4, 14},
		[]suit{},
		"",
		0,
	}
	s.True(hasThreeOfAKind(&input))
	s.Equal("three of a kind", input.order)
	s.Equal(2, input.rank)

	input = hand{
		[]int{2, 4, 4, 4, 8},
		[]suit{},
		"",
		0,
	}
	s.True(hasThreeOfAKind(&input))
	s.Equal("three of a kind", input.order)
	s.Equal(4, input.rank)

	input = hand{
		[]int{2, 3, 7, 7, 7},
		[]suit{},
		"",
		0,
	}
	s.True(hasThreeOfAKind(&input))
	s.Equal("three of a kind", input.order)
	s.Equal(7, input.rank)
}

func (s *kataSuite) Test_hasTwoPairs_returnsTrueIfTheGivenHandHasTwoPairs() {
	input := hand{
		[]int{2, 3, 7, 8, 9},
		[]suit{},
		"",
		0,
	}
	s.False(hasTwoPairs(&input))

	input = hand{
		[]int{2, 3, 3, 4, 5},
		[]suit{},
		"",
		0,
	}
	s.False(hasTwoPairs(&input))

	input = hand{
		[]int{2, 2, 7, 8, 8},
		[]suit{},
		"",
		0,
	}
	s.True(hasTwoPairs(&input))
	s.Equal("two pairs", input.order)
	s.Equal(8, input.rank)

	input = hand{
		[]int{3, 3, 5, 5, 8},
		[]suit{},
		"",
		0,
	}
	s.True(hasTwoPairs(&input))
	s.Equal("two pairs", input.order)
	s.Equal(5, input.rank)

	input = hand{
		[]int{2, 6, 6, 13, 13},
		[]suit{},
		"",
		0,
	}
	s.True(hasTwoPairs(&input))
	s.Equal("two pairs", input.order)
	s.Equal(13, input.rank)
}

func (s *kataSuite) Test_hasAPair_returnsTrueIfTheGivenHandHasOnlyOnePair() {
	input := hand{
		[]int{2, 5, 6, 8, 13},
		[]suit{},
		"",
		0,
	}
	s.False(hasAPair(&input))

	input = hand{
		[]int{2, 2, 6, 8, 13},
		[]suit{},
		"",
		0,
	}
	s.True(hasAPair(&input))
	s.Equal("pair", input.order)
	s.Equal(13, input.rank)

	input = hand{
		[]int{2, 6, 6, 8, 14},
		[]suit{},
		"",
		0,
	}
	s.True(hasAPair(&input))
	s.Equal("pair", input.order)
	s.Equal(14, input.rank)

	input = hand{
		[]int{2, 4, 5, 5, 7},
		[]suit{},
		"",
		0,
	}
	s.True(hasAPair(&input))
	s.Equal("pair", input.order)
	s.Equal(7, input.rank)

	input = hand{
		[]int{2, 4, 5, 12, 12},
		[]suit{},
		"",
		0,
	}
	s.True(hasAPair(&input))
	s.Equal("pair", input.order)
	s.Equal(5, input.rank)
}

func (s *kataSuite) Test_splitInput_returnsASliceOfStringsWithAHandPlayerEachOne() {
	input := "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"
	expected := []string{"Black: 2H 3D 5S 9C KD", "White: 2C 3H 4S 8C AH"}
	s.Equal(expected, splitInput(input))

	input = "Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 2S"
	expected = []string{"Black: 2H 4S 4C 2D 4H", "White: 2S 8S AS QS 2S"}
	s.Equal(expected, splitInput(input))
}

func (s *kataSuite) Test_valuesAndSuitsIn_givenAStringWithFiveCouplesOfValuesAndSuitsReturnsTwoSlicesWithTheValuesAndSuits() {
	input := "2H 3D 5S 9C KD"
	values, suits := valuesAndSuitsIn(input)
	s.Equal([]int{2, 3, 5, 9, 13}, values)
	s.Equal([]suit{"H", "D", "S", "C", "D"}, suits)

	input = "2H 4S 4C 2D 4H"
	values, suits = valuesAndSuitsIn(input)
	s.Equal([]int{2, 2, 4, 4, 4}, values)
	s.Equal([]suit{"H", "S", "C", "D", "H"}, suits)

	input = "2H 3H 4H 5H AH"
	values, suits = valuesAndSuitsIn(input)
	s.Equal([]int{2, 3, 4, 5, 14}, values)
	s.Equal([]suit{"H", "H", "H", "H", "H"}, suits)

	input = "2C 3S 4D 3H AS"
	values, suits = valuesAndSuitsIn(input)
	s.Equal([]int{2, 3, 3, 4, 14}, values)
	s.Equal([]suit{"C", "S", "D", "H", "S"}, suits)
}

func (s *kataSuite) Test_newHand_givenAStringOfFiveValueSuitCouplesReturnsAHand() {
	input := "2C 3H 4S 8C KH"
	expected := hand{
		[]int{2, 3, 4, 8, 13},
		[]suit{"C", "H", "S", "C", "H"},
		"",
		0,
	}
	s.Equal(expected, newHand(input))

	input = "2H 3D 5S 9C KD"
	expected = hand{
		[]int{2, 3, 5, 9, 13},
		[]suit{"H", "D", "S", "C", "D"},
		"",
		0,
	}
	s.Equal(expected, newHand(input))

	input = "4H 4D KD 4S 4C"
	expected = hand{
		[]int{4, 4, 4, 4, 13},
		[]suit{"H", "D", "D", "S", "C"},
		"",
		0,
	}
	s.Equal(expected, newHand(input))
}

func (s *kataSuite) Test_makePlayer_givenAnStringWithAPlayersNameAndAHandReturnsAPlayer() {
	input := "Black: 2H 3D 5S 9C KD"
	expected := player{
		"Black",
		hand{
			[]int{2, 3, 5, 9, 13},
			[]suit{"H", "D", "S", "C", "D"},
			"",
			0,
		},
	}
	s.Equal(expected, newPlayer(input))

	input = "White: 2C 3H 4S 8C AH"
	expected = player{
		"White",
		hand{
			[]int{2, 3, 4, 8, 14},
			[]suit{"C", "H", "S", "C", "H"},
			"",
			0,
		},
	}
	s.Equal(expected, newPlayer(input))
}
