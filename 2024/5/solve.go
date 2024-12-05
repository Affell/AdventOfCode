package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var rules = make(map[int][]int)
var updates [][]int

func main() {
	fmt.Println("Starting Day 5 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	rule := true
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			rule = false
			continue
		}
		if rule {
			parts := strings.Split(line, "|")
			a, _ := strconv.Atoi(parts[0])
			b, _ := strconv.Atoi(parts[1])
			rules[a] = append(rules[a], b)
		} else {
			update := []int{}
			for _, num := range strings.Split(line, ",") {
				n, _ := strconv.Atoi(num)
				update = append(update, n)
			}
			updates = append(updates, update)
		}
	}

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for _, update := range updates {
		if isOrdered(update) {
			count += update[len(update)/2]
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	count = 0
	for _, update := range updates {
		if !isOrdered(update) {
			fixed := fixOrder(append([]int(nil), update...), 0)
			count += fixed[len(fixed)/2]
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)
}

func isOrdered(update []int) bool {
	for i, n := range update {
		if after, exists := rules[n]; exists {
			for _, o := range after {
				if j := indexOf(update, o); j != -1 && j < i {
					return false
				}
			}
		}
	}
	return true
}

func fixOrder(update []int, iteration int) []int {
	if iteration > 100 {
		fmt.Printf("too many iterations: %v\n", update)
		return update
	}
	for i, n := range update {
		if after, exists := rules[n]; exists {
			for _, o := range after {
				if j := indexOf(update, o); j != -1 && j < i {
					update[i], update[j] = update[j], update[i]
				}
			}
		}
	}
	if isOrdered(update) {
		return update
	}
	return fixOrder(update, iteration+1)
}

func indexOf(slice []int, value int) int {
	for i, v := range slice {
		if v == value {
			return i
		}
	}
	return -1
}
