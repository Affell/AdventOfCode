package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var tab [][]int

func main() {
	fmt.Println("Starting Day 10 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		row := []int{}
		for _, e := range strings.Split(line, "") {
			num, _ := strconv.Atoi(e)
			row = append(row, num)
		}
		tab = append(tab, row)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
		return
	}

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for x := range tab {
		for y := range tab[0] {
			if tab[x][y] == 0 {
				count += getTrailHeadScore(x, y, nil)
			}
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	count = 0
	for x := range tab {
		for y := range tab[0] {
			if tab[x][y] == 0 {
				count += getTrailHeadRating(x, y, nil)
			}
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)
}

func getTrailHeadScore(x, y int, visited [][2]int) int {
	if visited == nil {
		visited = [][2]int{}
	}
	visited = append(visited, [2]int{x, y})
	if tab[x][y] == 9 {
		return 1
	} else {
		count := 0
		if x > 0 && tab[x-1][y] == tab[x][y]+1 && !contains(visited, [2]int{x - 1, y}) {
			count += getTrailHeadScore(x-1, y, visited)
		}
		if x < len(tab)-1 && tab[x+1][y] == tab[x][y]+1 && !contains(visited, [2]int{x + 1, y}) {
			count += getTrailHeadScore(x+1, y, visited)
		}
		if y > 0 && tab[x][y-1] == tab[x][y]+1 && !contains(visited, [2]int{x, y - 1}) {
			count += getTrailHeadScore(x, y-1, visited)
		}
		if y < len(tab[0])-1 && tab[x][y+1] == tab[x][y]+1 && !contains(visited, [2]int{x, y + 1}) {
			count += getTrailHeadScore(x, y+1, visited)
		}
		return count
	}
}

func getTrailHeadRating(x, y int, visited [][2]int) int {
	if visited == nil {
		visited = [][2]int{}
	}
	if tab[x][y] == 9 {
		return 1
	} else {
		count := 0
		if x > 0 && tab[x-1][y] == tab[x][y]+1 && !contains(visited, [2]int{x - 1, y}) {
			count += getTrailHeadRating(x-1, y, append(visited, [2]int{x, y}))
		}
		if x < len(tab)-1 && tab[x+1][y] == tab[x][y]+1 && !contains(visited, [2]int{x + 1, y}) {
			count += getTrailHeadRating(x+1, y, append(visited, [2]int{x, y}))
		}
		if y > 0 && tab[x][y-1] == tab[x][y]+1 && !contains(visited, [2]int{x, y - 1}) {
			count += getTrailHeadRating(x, y-1, append(visited, [2]int{x, y}))
		}
		if y < len(tab[0])-1 && tab[x][y+1] == tab[x][y]+1 && !contains(visited, [2]int{x, y + 1}) {
			count += getTrailHeadRating(x, y+1, append(visited, [2]int{x, y}))
		}
		return count
	}
}

func contains(slice [][2]int, item [2]int) bool {
	for _, v := range slice {
		if v == item {
			return true
		}
	}
	return false
}
