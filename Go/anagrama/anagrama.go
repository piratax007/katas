package anagrama

import (
	"fmt"
	"golang.org/x/exp/slices"
	"io/ioutil"
	"strings"

	"golang.org/x/exp/maps"
)

type word string

func transform(line string) []word {
	words := []word{}
	for _, w := range strings.Split(line, " ") {
		words = append(words, word(w))
	}

	return words
}

func wordsInDictionary(linesInDictionary []string) []word {
	words := []word{}

	for _, l := range linesInDictionary {
		words = append(words, transform(l)...)
	}
	return words
}

func fileReader(dictPath string) []word {
	fileContent, _ := ioutil.ReadFile(dictPath)
	lines := strings.Split(string(fileContent), "\n")

	return wordsInDictionary(lines)
}

type length int

func partitions(fileString []word) map[length][]word {
	filePartitions := map[length][]word{}

	for _, s := range fileString {
		filePartitions[length(len(s))] = append(filePartitions[length(len(s))], s)
	}

	keyList := maps.Keys(filePartitions)
	slices.Sort(keyList)
	fmt.Println(keyList)
	return filePartitions
}
