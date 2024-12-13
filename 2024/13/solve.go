package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting Day 13 solver")
	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}

	lines := strings.Split(string(data), "\n")
	c := []int{3, 1}
	var machines []map[string][]int

	for i := 0; i < len(lines); i += 4 {
		if i+2 >= len(lines) {
			break
		}
		machine := make(map[string][]int)
		machine["A"] = parseLine(lines[i])
		machine["B"] = parseLine(lines[i+1])
		machine["prize"] = parseLine(lines[i+2])
		machines = append(machines, machine)
	}

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for _, machine := range machines {
		_, fun := getMinTokens(machine, c, false)
		count += fun
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	count = 0
	for _, machine := range machines {
		_, fun := getMinTokens(machine, c, true)
		count += fun
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)
}

func parseLine(line string) []int {
	parts := strings.Split(line, ": ")[1]
	elements := strings.Split(parts, ", ")
	var result []int
	for _, e := range elements {
		num, _ := strconv.Atoi(e[2:])
		result = append(result, num)
	}
	return result
}

func getMinTokens(machine map[string][]int, c []int, part2 bool) ([2]int, int) {
	A := machine["A"]
	B := machine["B"]
	P := machine["prize"]

	if part2 {
		for i := range P {
			P[i] += 10000000000000
		}
	}

	a := float64(P[0]*B[1]-P[1]*B[0]) / float64(A[0]*B[1]-A[1]*B[0])
	b := float64(P[1]*A[0]-P[0]*A[1]) / float64(A[0]*B[1]-A[1]*B[0])
	if a == float64(int(a)) && b == float64(int(b)) {
		return [2]int{int(a), int(b)}, int(a)*c[0] + int(b)*c[1]
	}
	return [2]int{0, 0}, 0
}
