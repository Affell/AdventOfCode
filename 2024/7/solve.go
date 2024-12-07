package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func plusOperator(x, y int) int {
	return x + y
}

func multiplyOperator(x, y int) int {
	return x * y
}

func concatOperator(x, y int) int {
	res, _ := strconv.Atoi(fmt.Sprintf("%d%d", x, y))
	return res
}

func isPossible(target int, numbers []int, operators []func(int, int) int) bool {
	if len(numbers) == 0 {
		return target == 0
	}
	if len(numbers) == 1 {
		return numbers[0] == target
	}

	for _, op := range operators {
		res := op(numbers[0], numbers[1])
		tmp := append([]int{res}, numbers[2:]...)
		if isPossible(target, tmp, operators) {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println("Starting Day 7 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	calibrations := make(map[int][]int)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Split(line, ":")
		key, _ := strconv.Atoi(parts[0])
		values := strings.Fields(parts[1])
		var nums []int
		for _, v := range values {
			num, _ := strconv.Atoi(v)
			nums = append(nums, num)
		}
		calibrations[key] = nums
	}

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for k, v := range calibrations {
		if isPossible(k, v, []func(int, int) int{plusOperator, multiplyOperator}) {
			count += k
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	count = 0
	for k, v := range calibrations {
		if isPossible(k, v, []func(int, int) int{plusOperator, multiplyOperator, concatOperator}) {
			count += k
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)
}
