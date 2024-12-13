package main

import (
	"fmt"
	"os"
	"strings"
)

type Group struct {
	elements [][]int
	walls    [][][]int
}

func main() {
	fmt.Println("Starting Day 12 solver")

	data, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}

	lines := strings.Split(string(data), "\n")
	tab := make([][]rune, len(lines))
	for i, line := range lines {
		tab[i] = []rune(line)
	}

	var bfs func(x, y int, target rune, elements *[][]int, walls *[][][]int, visited *[][]int) bool
	bfs = func(x, y int, target rune, elements *[][]int, walls *[][][]int, visited *[][]int) bool {
		for _, v := range *visited {
			if v[0] == x && v[1] == y {
				return tab[x][y] == target
			}
		}
		*visited = append(*visited, []int{x, y})
		if x < 0 || x >= len(tab) || y < 0 || y >= len(tab[0]) || tab[x][y] != target {
			return false
		}
		*elements = append(*elements, []int{x, y})
		if !bfs(x-1, y, target, elements, walls, visited) {
			(*walls)[0] = append((*walls)[0], []int{x, y})
		}
		if !bfs(x+1, y, target, elements, walls, visited) {
			(*walls)[1] = append((*walls)[1], []int{x, y})
		}
		if !bfs(x, y-1, target, elements, walls, visited) {
			(*walls)[2] = append((*walls)[2], []int{x, y})
		}
		if !bfs(x, y+1, target, elements, walls, visited) {
			(*walls)[3] = append((*walls)[3], []int{x, y})
		}
		return true
	}

	fmt.Println("\n------------------------------\nComputing first part")
	var groups []Group
	var edges [][][]int
	var visited [][]int
	for i := range tab {
		for j := range tab[0] {
			if !contains(visited, []int{i, j}) {
				var elements [][]int
				walls := make([][][]int, 4)
				bfs(i, j, tab[i][j], &elements, &walls, &visited)
				var edge [][]int
				for _, element := range elements {
					if element[0] == 0 || !contains(elements, []int{element[0] - 1, element[1]}) {
						edge = append(edge, element)
					}
					if element[0] == len(tab)-1 || !contains(elements, []int{element[0] + 1, element[1]}) {
						edge = append(edge, element)
					}
					if element[1] == 0 || !contains(elements, []int{element[0], element[1] - 1}) {
						edge = append(edge, element)
					}
					if element[1] == len(tab[0])-1 || !contains(elements, []int{element[0], element[1] + 1}) {
						edge = append(edge, element)
					}
				}
				groups = append(groups, Group{elements, walls})
				edges = append(edges, edge)
				visited = append(visited, elements...)
			}
		}
	}

	price := 0
	for i := range edges {
		price += len(edges[i]) * len(groups[i].elements)
	}
	fmt.Printf("Answer : %d\n------------------------------\n", price)

	var sideBfs func(x, y int, group, elements, visited *[][]int)
	sideBfs = func(x, y int, group, elements, visited *[][]int) {
		for _, v := range *visited {
			if v[0] == x && v[1] == y {
				return
			}
		}
		*visited = append(*visited, []int{x, y})
		if x < 0 || x >= len(tab) || y < 0 || y >= len(tab[0]) || !contains(*group, []int{x, y}) {
			return
		}
		*elements = append(*elements, []int{x, y})
		sideBfs(x-1, y, group, elements, visited)
		sideBfs(x+1, y, group, elements, visited)
		sideBfs(x, y-1, group, elements, visited)
		sideBfs(x, y+1, group, elements, visited)
	}

	fmt.Println("\n------------------------------\nComputing second part")
	var sides []int
	for _, group := range groups {
		var groupSides [][]int
		for _, dir := range group.walls {
			var visited [][]int
			for _, wall := range dir {
				if contains(visited, []int{wall[0], wall[1]}) {
					continue
				}
				var side [][]int
				sideBfs(wall[0], wall[1], &dir, &side, &visited)
				groupSides = append(groupSides, side...)
				visited = append(visited, side...)
			}
		}
		sides = append(sides, len(groupSides))
	}

	price = 0
	for i := range groups {
		price += sides[i] * len(groups[i].elements)
	}
	fmt.Printf("Answer : %d\n------------------------------\n", price)
}

func contains(slice [][]int, item []int) bool {
	for _, v := range slice {
		if v[0] == item[0] && v[1] == item[1] {
			return true
		}
	}
	return false
}
