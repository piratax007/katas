package day1

type triplet struct {
	first  depth
	second depth
	third  depth
}

func retrieveATriplet(index int, measures []measure) triplet {
	t := triplet{
		first:  measures[index].value,
		second: measures[index+1].value,
		third:  measures[index+2].value,
	}
	return t
}

func (t *triplet) sumTriplet() depth {
	return t.first + t.second + t.third
}

func (t *triplet) isDeeperThan(other triplet) bool {
	return t.sumTriplet() > other.sumTriplet()
}

func countTripletsIncrements(measures []measure) int {
	result := 0

	measuresWithoutLastTriplet := measures[:len(measures)-3]
	for i := range measuresWithoutLastTriplet {
		currentTriplet := retrieveATriplet(i, measures)
		nextTriplet := retrieveATriplet(i+1, measures)

		if nextTriplet.isDeeperThan(currentTriplet) {
			result += 1
		}
	}

	return result
}

func solveForTriplets(tripletsFile string) int {
	measures, err := readInputDataFrom(tripletsFile)
	if err != nil {
		panic(err)
	}

	return countTripletsIncrements(measures)
}
