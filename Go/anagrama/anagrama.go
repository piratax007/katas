package anagrama

import (
	"golang.org/x/exp/maps"
	"golang.org/x/exp/slices"
	"io/ioutil"
	"sort"
	"strings"
)

type word string

func wordsInDictionary(linesInDictionary []string) (words []word) {
	for _, l := range linesInDictionary {
		words = append(words, transform(strings.Split(l, " "), func(w string) word {
			return word(strings.ToLower(w))
		})...)
	}

	return
}

func fileReader(dictPath string) []word {
	fileContent, _ := ioutil.ReadFile(dictPath)
	fileLines := strings.Split(string(fileContent), "\n")
	cleanLines := []string{}
	for _, l := range fileLines {
		cleanLines = append(cleanLines, strings.Join(strings.Fields(l), " "))
	}

	return wordsInDictionary(cleanLines)
}

func partitions(fileString []word) map[int][]word {
	dictPartitions := map[int][]word{}
	for _, s := range fileString {
		dictPartitions[len(s)] = append(dictPartitions[len(s)], s)
	}

	return dictPartitions
}

func complementaryLists(wM map[int][]word, l1, l2 int) (cl1, cl2 []word) {
	if wM[l1] == nil || wM[l2] == nil {
		return nil, nil
	}

	return wM[l1], wM[l2]
}

func checkAnagram(w1, w2, w3 word) bool {
	possibleAnagramCharacters := strings.Split(string(w1+w2), "")
	w3Characters := strings.Split(string(w3), "")
	sort.Strings(possibleAnagramCharacters)
	sort.Strings(w3Characters)
	if strings.Join(possibleAnagramCharacters, "") == strings.Join(w3Characters, "") {
		return true
	}

	return false
}

func lengthsList(wM map[int][]word, w word) (kLFiltered []int) {
	kL := maps.Keys(wM)
	slices.Sort(kL)
	return filter(kL, isLeaserThan(len(w)))
}

func findAnagrams(filePath string, w word) (anagrams []word) {
	wM := partitions(fileReader(filePath))
	kL := lengthsList(wM, w)
	for len(kL) > 0 {
		complement := len(w) - kL[0]
		if slices.Contains(kL, complement) {
			l1, l2 := complementaryLists(wM, kL[0], complement)
			for _, w1 := range l1 {
				for _, w2 := range l2 {
					if checkAnagram(w1, w2, w) {
						anagrams = append(anagrams, []word{w1, w2}...)
					}
				}
			}
		}
		kL = kL[1:]
	}
	return
}
