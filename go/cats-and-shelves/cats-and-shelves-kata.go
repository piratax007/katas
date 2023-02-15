package main

import "fmt"

type cat struct {
	start      int
	finish     int
	distance   int
	countJumps int
}

func (c *cat) countingJumps() {
	switch c.distance {
	case 0:
		break
	case 1, 3:
		c.countJumps += 1
	case 2:
		c.start += 1
		c.countJumps += 1
		c.distance -= 1
		c.countingJumps()
	default:
		c.start += 3
		c.countJumps += 1
		c.distance -= 3
		c.countingJumps()
	}
}

func newCat(start, finish int) *cat {
	return &cat{
		start:      start,
		finish:     finish,
		distance:   finish - start,
		countJumps: 0,
	}
}
func cats(start, finish int) int {
	kitty := newCat(start, finish)

	kitty.countingJumps()

	return kitty.countJumps
}

func main() {
	fmt.Println(cats(2, 4))
}
