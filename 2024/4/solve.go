package main

import (
	"bufio"
	"fmt"
	"os"
)

var translate = map[rune]int{
	'X': 0,
	'M': 1,
	'A': 2,
	'S': 3,
}

var tab [][]int

func main() {
	fmt.Println("Starting Day 4 solver")

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
		for _, char := range line {
			row = append(row, translate[char])
		}
		tab = append(tab, row)
	}

	fmt.Println("\n------------------------------\nComputing first part")
	count := 0
	for i := range tab {
		for j := range tab[0] {
			if tab[i][j] == 0 {
				count += len(getWords(i, j, 0, 0, 1))
			}
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", count)

	fmt.Println("\n------------------------------\nComputing second part")
	words := make(map[[2]int][][2]int)
	var crossedWords [][6]int
	for i := range tab {
		for j := range tab[0] {
			if tab[i][j] == 1 {
				found := getWords(i, j, 0, 0, 2)
				for _, w := range found {
					x, y, dirx, diry := w[0], w[1], w[2], w[3]
					if dirx == 0 || diry == 0 {
						continue
					}
					key := [2]int{x, y}
					if _, exists := words[key]; !exists {
						words[key] = append(words[key], [2]int{dirx, diry})
					} else {
						for _, dir := range words[key] {
							dx, dy := dir[0], dir[1]
							if dx*dirx+dy*diry == 0 {
								crossedWords = append(crossedWords, [6]int{x, y, dirx, diry, dx, dy})
								words[key] = removeDirection(words[key], dir)
								break
							}
						}
					}
				}
			}
		}
	}
	fmt.Printf("Answer : %d\n------------------------------\n", len(crossedWords))
}

func getWords(x, y, dirx, diry, target int) [][4]int {
	if x < 0 || x >= len(tab) || y < 0 || y >= len(tab[0]) {
		return nil
	}
	if target == 4 && tab[x][y] == 3 {
		return [][4]int{{x, y, dirx, diry}}
	}
	if tab[x][y] == target-1 {
		if dirx == 0 && diry == 0 {
			var words [][4]int
			directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {-1, -1}, {-1, 1}, {1, -1}, {1, 1}}
			for _, dir := range directions {
				newWords := getWords(x+dir[0], y+dir[1], dir[0], dir[1], target+1)
				words = append(words, newWords...)
			}
			return words
		} else {
			return getWords(x+dirx, y+diry, dirx, diry, target+1)
		}
	}
	return nil
}

func removeDirection(directions [][2]int, dir [2]int) [][2]int {
	for i, d := range directions {
		if d == dir {
			return append(directions[:i], directions[i+1:]...)
		}
	}
	return directions
}
