package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	fmt.Println("Starting Day 8 solver")

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

	tab := make([][]rune, len(data))
	for i := range tab {
		tab[i] = make([]rune, len(data[0]))
	}

	locations := make(map[rune][][2]int)
	for i := 0; i < len(data); i++ {
		for j := 0; j < len(data[i]); j++ {
			c := rune(data[i][j])
			tab[i][j] = c
			if c != '.' {
				locations[c] = append(locations[c], [2]int{i, j})
			}
		}
	}

	fmt.Println("\n------------------------------\nComputing first part")
	antinodes := getAntinodes(tab, locations)
	fmt.Printf("Answer : %d\n------------------------------\n", len(antinodes))

	fmt.Println("\n------------------------------\nComputing second part")
	harmonicAntinodes := getAntinodesHarmonics(tab, locations)
	fmt.Printf("Answer : %d\n------------------------------\n", len(harmonicAntinodes))
}

func getAntinodes(tab [][]rune, locations map[rune][][2]int) [][2]int {
	var antinodes [][2]int
	for k := range locations {
		if len(locations[k]) == 1 {
			continue
		}
		for i := 0; i < len(locations[k]); i++ {
			for j := i + 1; j < len(locations[k]); j++ {
				p1 := locations[k][i]
				p2 := locations[k][j]
				diff := [2]int{p2[0] - p1[0], p2[1] - p1[1]}
				firstAntinode := [2]int{p1[0] - diff[0], p1[1] - diff[1]}
				secondAntinode := [2]int{p2[0] + diff[0], p2[1] + diff[1]}
				if firstAntinode[0] >= 0 && firstAntinode[0] < len(tab) && firstAntinode[1] >= 0 && firstAntinode[1] < len(tab[0]) && !contains(antinodes, firstAntinode) {
					antinodes = append(antinodes, firstAntinode)
				}
				if secondAntinode[0] >= 0 && secondAntinode[0] < len(tab) && secondAntinode[1] >= 0 && secondAntinode[1] < len(tab[0]) && !contains(antinodes, secondAntinode) {
					antinodes = append(antinodes, secondAntinode)
				}
			}
		}
	}
	return antinodes
}

func getAntinodesHarmonics(tab [][]rune, locations map[rune][][2]int) [][2]int {
	var antinodes [][2]int
	for k := range locations {
		if len(locations[k]) == 1 {
			continue
		}
		for i := 0; i < len(locations[k]); i++ {
			for j := i + 1; j < len(locations[k]); j++ {
				p1 := locations[k][i]
				p2 := locations[k][j]
				if !contains(antinodes, p1) {
					antinodes = append(antinodes, p1)
				}
				if !contains(antinodes, p2) {
					antinodes = append(antinodes, p2)
				}
				diff := [2]int{p2[0] - p1[0], p2[1] - p1[1]}
				firstAntinode := [2]int{p1[0] - diff[0], p1[1] - diff[1]}
				for firstAntinode[0] >= 0 && firstAntinode[0] < len(tab) && firstAntinode[1] >= 0 && firstAntinode[1] < len(tab[0]) {
					if !contains(antinodes, firstAntinode) {
						antinodes = append(antinodes, firstAntinode)
					}
					firstAntinode = [2]int{firstAntinode[0] - diff[0], firstAntinode[1] - diff[1]}
				}
				secondAntinode := [2]int{p2[0] + diff[0], p2[1] + diff[1]}
				for secondAntinode[0] >= 0 && secondAntinode[0] < len(tab) && secondAntinode[1] >= 0 && secondAntinode[1] < len(tab[0]) {
					if !contains(antinodes, secondAntinode) {
						antinodes = append(antinodes, secondAntinode)
					}
					secondAntinode = [2]int{secondAntinode[0] + diff[0], secondAntinode[1] + diff[1]}
				}
			}
		}
	}
	return antinodes
}

func contains(slice [][2]int, item [2]int) bool {
	for _, v := range slice {
		if v == item {
			return true
		}
	}
	return false
}
