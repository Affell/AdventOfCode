package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("Starting Day 9 solver")

	file, err := os.Open("input.txt")
	if err != nil {
		fmt.Println("Your input file must be named input.txt and placed in this directory")
		return
	}
	defer file.Close()

	var data string
	scanner := bufio.NewScanner(file)
	if scanner.Scan() {
		data = scanner.Text()
	} else {
		fmt.Println("Your input file must contain one line of data")
		return
	}

	line := strings.TrimSpace(string(data))

	fmt.Println("\n------------------------------\nComputing first part")
	fs := translateDiskMap(line)
	defragged := defrag(fs)
	result := checksum(defragged)
	fmt.Printf("Answer : %d\n------------------------------\n", result)

	fmt.Println("\n------------------------------\nComputing second part")
	defragged = defragBlock(fs)
	result = checksum(defragged)
	fmt.Printf("Answer : %d\n------------------------------\n", result)
}

func translateDiskMap(line string) []interface{} {
	var fs []interface{}
	index := 0
	for i := 0; i < len(line); i++ {
		count, _ := strconv.Atoi(string(line[i]))
		if i%2 == 0 {
			for j := 0; j < count; j++ {
				fs = append(fs, index)
			}
			index++
		} else {
			for j := 0; j < count; j++ {
				fs = append(fs, ".")
			}
		}
	}
	return fs
}

func defrag(fs []interface{}) []interface{} {
	defragged := make([]interface{}, len(fs))
	copy(defragged, fs)
	firstFree := indexOf(defragged, ".")
	for i := 0; i < len(fs); i++ {
		if firstFree > len(fs)-i-1 {
			break
		}
		e := fs[len(fs)-i-1]
		if e != "." {
			defragged[firstFree] = e
			defragged[len(fs)-i-1] = "."
			found := false
			for j := firstFree + 1; j < len(fs); j++ {
				if defragged[j] == "." {
					firstFree = j
					found = true
					break
				}
			}
			if !found {
				break
			}
		}
	}
	return defragged
}

func checksum(fs []interface{}) int {
	sum := 0
	for i := 1; i < len(fs); i++ {
		if fs[i] != "." {
			sum += fs[i].(int) * i
		}
	}
	return sum
}

func defragBlock(fs []interface{}) []interface{} {
	defragged := make([]interface{}, len(fs))
	copy(defragged, fs)
	firstFree, size := getNextFree(defragged, 0)
	for i := 0; i < len(fs); i++ {
		if firstFree > len(fs)-i-1 || firstFree == -1 {
			break
		}
		e := fs[len(fs)-i-1]
		if i < len(fs)-1 && fs[len(fs)-i-2] == e {
			size++
			continue
		}
		if e != "." {
			tmpFree := firstFree
			for tmpFree < len(fs) && size > 0 && defragged[tmpFree] == "." {
				tmpFree++
			}
			if tmpFree == len(fs) {
				size = 1
				continue
			}
			for j := 0; j < size; j++ {
				defragged[tmpFree+j] = e
				defragged[len(fs)-i-1+j] = "."
			}
			size = 1
			if tmpFree == firstFree {
				firstFree, size = getNextFree(defragged, tmpFree+size)
			}
		} else {
			size = 1
		}
	}
	return defragged
}

func getNextFree(fs []interface{}, start int) (int, int) {
	first := -1
	count := 0
	for i := start; i < len(fs); i++ {
		if fs[i] == "." {
			if first == -1 {
				first = i
			}
			count++
		} else if first != -1 {
			break
		}
	}
	return first, count
}

func indexOf(slice []interface{}, value interface{}) int {
	for i, v := range slice {
		if v == value {
			return i
		}
	}
	return -1
}
