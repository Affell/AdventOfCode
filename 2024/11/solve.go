package main

import (
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting Day 11 solver")

	data, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal("Your input file must be named input.txt and placed in this directory")
	}

	lines := strings.Split(string(data), "\n")
	rocksStr := strings.Split(lines[0], " ")
	rocks := make([]int, len(rocksStr))
	for i, s := range rocksStr {
		rocks[i], _ = strconv.Atoi(s)
	}

	fmt.Println("\n------------------------------\nComputing first part")
	r := blink(rocks, 25)
	count := 0
	for _, v := range r {
		count += v
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	r = blink(rocks, 75)
	count = 0
	for _, v := range r {
		count += v
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)
}

func blink(rocks []int, nbBlinks int) map[int]int {
	grouped := make(map[int]int)
	for _, r := range rocks {
		grouped[r]++
	}

	for i := 0; i < nbBlinks; i++ {
		next := make(map[int]int)
		for n, count := range grouped {
			if n == 0 {
				next[1] += count
			} else if len(strconv.Itoa(n))%2 == 0 {
				strNb := strconv.Itoa(n)
				left, _ := strconv.Atoi(strNb[:len(strNb)/2])
				right, _ := strconv.Atoi(strNb[len(strNb)/2:])
				next[left] += count
				next[right] += count
			} else {
				next[n*2024] += count
			}
		}
		grouped = next
	}

	return grouped
}
