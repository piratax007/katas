package anagrama

import (
	"os"
	"path"
	"testing"

	"github.com/stretchr/testify/suite"
)

type kataSuite struct {
	suite.Suite
	tdir string
}

func TestKataSuite(t *testing.T) {
	suite.Run(t, new(kataSuite))
}

func (s *kataSuite) SetupTest() {
	s.tdir = s.T().TempDir()
}

func (s *kataSuite) createFileWithContent(dir, fileName, content string) {
	e := os.WriteFile(path.Join(dir, fileName), []byte(content), 0666)
	s.Nil(e)
}

func (s *kataSuite) Test_fileReader_returnsASliceOfWordsThatFileGivenContain() {
	s.createFileWithContent(s.tdir, "wordsTest.txt", "tea sun apple phone car computer")
	pathFile := path.Join(s.tdir, "wordsTest.txt")
	words := fileReader(pathFile)
	expected := []word{
		"tea",
		"sun",
		"apple",
		"phone",
		"car",
		"computer",
	}
	s.Equal(expected, words)

	s.createFileWithContent(s.tdir, "wordsTest.txt", "tea sun apple phone car computer\nsoup coffee cup mouse")
	words = fileReader(pathFile)
	expected = []word{
		"tea",
		"sun",
		"apple",
		"phone",
		"car",
		"computer",
		"soup",
		"coffee",
		"cup",
		"mouse",
	}
	s.Equal(expected, words)

	s.createFileWithContent(s.tdir, "wordsTest.txt", "Milk\nAlcohol\nlaptop\nscreen\nMathematics\nuniverse")
	words = fileReader(pathFile)
	expected = []word{
		"milk",
		"alcohol",
		"laptop",
		"screen",
		"mathematics",
		"universe",
	}
	s.Equal(expected, words)
}

func (s *kataSuite) Test_partitions_returnsAMapWithOnlyOneEntryIfOnlyOneWordIsGiven() {
	wordsMap := partitions([]word{"Unique"})

	expected := map[int][]word{
		6: {"Unique"},
	}

	s.Equal(expected, wordsMap)
}

func (s *kataSuite) Test_partitions_returnsAMapWithLengthsAsKeysAndSlicesOfWordsAsValues() {
	wordsMap := partitions([]word{"tea", "apple", "sun", "phone", "computer", "car"})

	expected := map[int][]word{
		3: {"tea", "sun", "car"},
		8: {"computer"},
		5: {"apple", "phone"},
	}

	s.Equal(expected, wordsMap)
}

func (s *kataSuite) Test_complementaryLists_returnsTwoEmptyListsWhenNeitherOfTheLengthsGivenAreKeysInTheMap() {
	wordsMap := map[int][]word{
		4: {"visa", "taxi"},
		5: {"final", "focus", "forum"},
		6: {"studio", "signal", "report"},
	}
	var length1 int = 3
	var length2 int = 7
	list1, list2 := complementaryLists(wordsMap, length1, length2)
	s.Nil(list1)
	s.Nil(list2)
}

func (s *kataSuite) Test_complementaryLists_returnsTwoEmptyListsWhenOnlyOneOfTheLengthsGiverIsAKeyInTheMap() {
	wordsMap := map[int][]word{
		4: {"visa", "taxi"},
		5: {"final", "focus", "forum"},
		6: {"studio", "signal", "report"},
	}
	var length1 int = 5
	var length2 int = 8
	list1, list2 := complementaryLists(wordsMap, length1, length2)
	s.Nil(list1)
	s.Nil(list2)

	length1 = 3
	length2 = 4
	list1, list2 = complementaryLists(wordsMap, length1, length2)
	s.Nil(list1)
	s.Nil(list2)
}

func (s *kataSuite) Test_complementaryLists_returnsTwoListsFromAMapWhenThisContainsTwoKeysCorrespondingWithTwoIntegersGiven() {
	wordsMap := map[int][]word{
		4: {"visa", "taxi"},
		5: {"final", "focus", "forum"},
		6: {"studio", "signal", "report"},
	}
	var length1 int = 4
	var length2 int = 6
	list1, list2 := complementaryLists(wordsMap, length1, length2)
	expectedList1 := []word{"visa", "taxi"}
	expectedList2 := []word{"studio", "signal", "report"}
	s.Equal(expectedList1, list1)
	s.Equal(expectedList2, list2)

	length1 = 5
	length2 = 5
	list1, list2 = complementaryLists(wordsMap, length1, length2)
	expectedList1 = []word{"final", "focus", "forum"}
	expectedList2 = []word{"final", "focus", "forum"}
	s.Equal(expectedList1, list1)
	s.Equal(expectedList2, list2)
}

func (s *kataSuite) Test_checkAnagramWith_returnsTrueIfTheFirstTwoWordsConformsAnAnagramOfTheThird() {
	c := checkAnagram("dirty", "room", "dormitory")
	s.True(c)

	c = checkAnagram("moon", "starer", "astronomer")
	s.True(c)
}

func (s *kataSuite) Test_checkAnagram_returnsFalseIfTheFirstTwoWordsCannotConformsAnAnagramOfTheThird() {
	c := checkAnagram("bed", "room", "dormitory")
	s.False(c)

	c = checkAnagram("phones", "juices", "mathematician")
	s.False(c)
}

func (s *kataSuite) Test_findAnagrams_givenAFileAndAWordReturnsNilIfNeitherTowWordsInTheFileConformsAnAnagramOfTheWordGiven() {
	s.createFileWithContent(s.tdir, "wordsTest.txt", "visa taxi final focus forum studio signal report")
	pathFile := path.Join(s.tdir, "wordsTest.txt")

	var w word = "mathematician"
	anagrams := findAnagrams(pathFile, w)
	s.Nil(anagrams)
}

func (s *kataSuite) Test_findAnagrams_returnASliceWithOnlyTwoWordsWhenTheFileDoesNotContainsMoreWordsThatConformsAnAnagramOfTheGivenWord() {
	s.createFileWithContent(s.tdir, "wordsTest.txt", "visa final studio room focus signal taxi forum report dirty")
	pathFile := path.Join(s.tdir, "wordsTest.txt")
	var w word = "dormitory"
	anagram := findAnagrams(pathFile, w)
	expected := []word{
		"room",
		"dirty",
	}
	s.Equal(expected, anagram)

	s.createFileWithContent(s.tdir, "wordsTest.txt", "tea visa final studio signal focus room sun car taxi forum starer moon dirty report")
	pathFile = path.Join(s.tdir, "wordsTest.txt")
	w = "astronomer"
	anagram = findAnagrams(pathFile, w)
	expected = []word{
		"moon",
		"starer",
	}
	s.Equal(expected, anagram)
}

func (s *kataSuite) Test_findAnagrams_returnsASliceWithAllTheWordsThatConformsAnagramsFromTheGivenWord() {
	s.createFileWithContent(s.tdir, "wordsTest.txt", "tea visa final studio\nsignal sing gins focus\nroom sun car taxi\nforum starer redundant moon\ndirty report")
	pathFile := path.Join(s.tdir, "wordsTest.txt")
	var w word = "understanding"
	anagrams := findAnagrams(pathFile, w)
	expected := []word{
		"sing",
		"redundant",
		"gins",
		"redundant",
	}
	s.Equal(expected, anagrams)

	pathFile = "wordlist.txt"
	w = "documenting"
	anagrams = findAnagrams(pathFile, w)
	expected = []word{
		"td", "mucinogen", "ug", "condiment", "cog", "indument", "cog",
		"unminted", "den", "cognitum", "dim", "uncogent", "dum", "incogent",
		"end", "cognitum", "gin", "document", "got", "unminced", "ing",
		"document", "ing", "document", "mid", "uncogent", "mud", "incogent",
		"ned", "cognitum", "nig", "document", "tog", "unminced", "cond",
		"mugient", "dont", "mucigen", "dung", "centimo", "dung", "entomic",
		"dung", "tecomin", "dunt", "genomic", "guti", "condemn", "meng",
		"conduit", "meng", "duction", "meng", "noctuid", "mong", "uncited",
		"mung", "condite", "mung", "ctenoid", "mute", "condign", "tong",
		"mucedin", "tume", "condign", "tund", "genomic", "tung", "demonic",
		"coned", "tignum", "cutin", "gnomed", "demon", "gutnic", "demon",
		"gutnic", "dingo", "centum", "doing", "centum", "educt", "mignon",
		"genom", "induct", "gnome", "induct", "gondi", "centum", "gonid",
		"centum", "gonne", "dictum", "incut", "gnomed", "medoc", "tuning",
		"metic", "dungon", "tuned", "coming", "tuned", "gnomic", "tunic",
		"gnomed", "undim", "cogent",
	}
	s.Equal(expected, anagrams)
}
