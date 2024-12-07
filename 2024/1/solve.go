package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting Day 1 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	var data []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	var right, left []int
	for _, l := range data {
		parts := strings.Split(l, "   ")
		le, _ := strconv.Atoi(strings.TrimSpace(parts[0]))
		ri, _ := strconv.Atoi(strings.TrimSpace(parts[1]))
		left = append(left, le)
		right = append(right, ri)
	}

	sort.Ints(right)
	sort.Ints(left)

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for i := range left {
		count += abs(left[i] - right[i])
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	count2 := 0
	for _, n := range left {
		count2 += n * countOccurrences(right, n)
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count2)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func countOccurrences(arr []int, target int) int {
	count := 0
	for _, v := range arr {
		if v == target {
			count++
		}
	}
	return count
}
