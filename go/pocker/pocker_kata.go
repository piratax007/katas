package main

import (
	"github.com/TectusDreamlab/go-common-utils/slice"
	"sort"
	"strings"
)

type suit string
type hand struct {
	values []int
	suits  []suit
	order  string
	rank   int
}

func foreach[T any](values []T, f func(T)) {
	for _, v := range values {
		f(v)
	}
}

func hasCoincidences[T comparable](values []T) bool {
	coincidences := 0
	foreach(values[1:], func(v T) {
		if v == values[0] {
			coincidences += 1
		}
	})

	return coincidences == len(values[1:])
}

func isFlush(h *hand) bool {
	if hasCoincidences(h.suits) {
		h.order = "flush"
		h.rank = h.values[4]
		return true
	}

	return false
}

func sum(integers []int) int {
	result := 0
	foreach(integers, func(i int) {
		result += i
	})

	return result
}

func changeAValue(h *hand) {
	if h.values[4] == 14 && sum(h.values[:4]) == 14 {
		h.values[4] = 1
		sort.Ints(h.values)
	}
}

func isStraight(h *hand) bool {
	changeAValue(h)

	if sum(h.values) == (5 * (h.values[0] + h.values[4]) / 2) {
		h.order = "straight"
		h.rank = h.values[4]
		return true
	}

	return false
}

func isStraightFlush(h *hand) bool {
	if isStraight(h) && isFlush(h) {
		h.order = "straight flush"
		return true
	}

	return false
}

func findCoincidencesIn(h *hand, partitions [][]int, order string) bool {
	for _, p := range partitions {
		if hasCoincidences(p) {
			h.order = order
			h.rank = p[0]
			return true
		}
	}

	return false
}

func hasFourOfAKind(h *hand) bool {
	partitions := [][]int{h.values[:4], h.values[1:]}

	return findCoincidencesIn(h, partitions, "four of a kind")
}

func isFullHouse(h *hand) bool {
	if hasCoincidences(h.values[:3]) && hasCoincidences(h.values[3:]) {
		h.order = "full house"
		h.rank = h.values[:3][2]
		return true
	}

	if hasCoincidences(h.values[2:]) && hasCoincidences(h.values[:2]) {
		h.order = "full house"
		h.rank = h.values[2:][2]
		return true
	}

	return false
}

func hasThreeOfAKind(h *hand) bool {
	partitions := [][]int{h.values[:3], h.values[1:4], h.values[2:]}

	return findCoincidencesIn(h, partitions, "three of a kind")
}

func hasTwoPairs(h *hand) bool {
	partitions := [][]int{h.values[:2], h.values[1:3], h.values[2:4], h.values[3:]}
	countPairs := 0
	ranks := []int{}

	for _, p := range partitions {
		if p[0] == p[1] {
			countPairs += 1
			ranks = append(ranks, p[1])
		}
	}

	if countPairs == 2 {
		h.order = "two pairs"
		h.rank = ranks[1]
		return true
	}

	return false
}

func hasAPair(h *hand) bool {
	twoSizePartitions := [][]int{h.values[:2], h.values[1:3], h.values[2:4], h.values[3:]}
	complementaryPartitions := [][]int{h.values[2:], h.values[3:], h.values[:2], h.values[:3]}

	for i := range twoSizePartitions {
		if hasCoincidences(twoSizePartitions[i]) && !hasCoincidences(complementaryPartitions[i]) {
			h.order = "pair"
			if slice.ContainsInt(twoSizePartitions[i], h.values[4]) {
				h.rank = h.values[2]
				return true
			}
			h.rank = h.values[4]
			return true
		}
	}
	return false
}

func splitInput(input string) []string {
	return strings.Split(input, "  ")
}

var valuesEquivalence = map[string]int{
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"T": 10,
	"J": 11,
	"Q": 12,
	"K": 13,
	"A": 14,
}

func valuesAndSuitsIn(input string) (values []int, suits []suit) {
	cards := strings.Split(input, " ")
	foreach(cards, func(c string) {
		valueSuitPair := strings.Split(c, "")
		values = append(values, valuesEquivalence[valueSuitPair[0]])
		suits = append(suits, suit(valueSuitPair[1]))
	})

	sort.Ints(values)

	return values, suits
}

func newHand(input string) hand {
	result := hand{}

	result.values, result.suits = valuesAndSuitsIn(input)

	return result
}

type player struct {
	name string
	hand hand
}

func newPlayer(input string) player {
	data := strings.Split(input, ": ")
	return player{
		data[0],
		newHand(data[1]),
	}
}

func main() {
	/*	input := "Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH"

		partialInputs := splitInput(input)

		player1 := newPlayer(partialInputs[0])
		player2 := newPlayer(partialInputs[1])*/
}
