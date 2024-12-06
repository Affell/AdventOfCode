package main

import (
	"bufio"
	"fmt"
	"os"
)

var tab [][]rune
var initPos [4]int

func main() {
	fmt.Println("Starting Day 6 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		tmp := []rune(line)
		for j, c := range tmp {
			switch c {
			case '^':
				initPos = [4]int{len(tab), j, -1, 0}
			case 'v':
				initPos = [4]int{len(tab), j, 1, 0}
			case '<':
				initPos = [4]int{len(tab), j, 0, -1}
			case '>':
				initPos = [4]int{len(tab), j, 0, 1}
			}
		}
		tab = append(tab, tmp)
	}
	if initPos == [4]int{} {
		fmt.Println("No initial direction found")
		return
	}

	fmt.Println("\n------------------------------\nComputing first part")
	positions := computeVisits(initPos[0], initPos[1], initPos[2], initPos[3])
	fmt.Printf("Answer : %d\n------------------------------\n", len(positions))

	fmt.Println("\n------------------------------\nComputing second part")
	loops := countLoopPossibilities(initPos[0], initPos[1], initPos[2], initPos[3], positions)
	fmt.Printf("Answer : %d\n------------------------------\n", len(loops))
}

func turnRight(dx, dy int) (int, int) {
	switch {
	case dx == 0 && dy == 1:
		return 1, 0
	case dx == 1 && dy == 0:
		return 0, -1
	case dx == 0 && dy == -1:
		return -1, 0
	case dx == -1 && dy == 0:
		return 0, 1
	}
	return 0, 0
}

func computeVisits(x, y, dx, dy int) map[[2]int]struct{} {
	visits := make(map[[2]int]struct{})
	visits[[2]int{x, y}] = struct{}{}
	for {
		x += dx
		y += dy
		if x < 0 || x >= len(tab) || y < 0 || y >= len(tab[0]) {
			break
		}
		if tab[x][y] == '#' {
			x -= dx
			y -= dy
			dx, dy = turnRight(dx, dy)
			continue
		}
		visits[[2]int{x, y}] = struct{}{}
	}
	return visits
}

func countLoopPossibilities(startX, startY, startDx, startDy int, visitedPos map[[2]int]struct{}) [][2]int {
	var loops [][2]int
	for pos := range visitedPos {
		tab[pos[0]][pos[1]] = '#'
		x, y, dx, dy := startX, startY, startDx, startDy
		visited := make(map[[4]int]struct{})
		for {
			x += dx
			y += dy
			if x < 0 || x >= len(tab) || y < 0 || y >= len(tab[0]) {
				break
			}
			if tab[x][y] == '#' {
				x -= dx
				y -= dy
				state := [4]int{x, y, dx, dy}
				if _, found := visited[state]; found {
					loops = append(loops, pos)
					break
				}
				visited[state] = struct{}{}
				dx, dy = turnRight(dx, dy)
				continue
			}
		}
		tab[pos[0]][pos[1]] = '.'
	}
	return loops
}
