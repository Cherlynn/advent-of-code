package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strings"
)

var WINDOW_SIZE int = 4

func main() {
	part1()
	part2()
}

func part1() {
	WINDOW_SIZE = 4
	input_file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer input_file.Close()
	scanner := bufio.NewScanner(input_file)

	for scanner.Scan() {
		signal := scanner.Text()
		for index, _ := range signal[:len(signal)-WINDOW_SIZE] {
			window := signal[index : index+WINDOW_SIZE]
			if is_all_unique(window) {
				fmt.Println(index + WINDOW_SIZE)
				return
			}
		}
	}
}

func part2() {
	WINDOW_SIZE = 14
	input_file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer input_file.Close()
	scanner := bufio.NewScanner(input_file)

	for scanner.Scan() {
		signal := scanner.Text()
		for index, _ := range signal[:len(signal)-WINDOW_SIZE] {
			window := signal[index : index+WINDOW_SIZE]
			if is_all_unique(window) {
				fmt.Println(index + WINDOW_SIZE)
				return
			}
		}
	}
}

func is_all_unique(window string) (is_all_unique bool) {
	window_strings := strings.Split(window, "")
	sort.Strings(window_strings)
	for window_index, window_string := range window_strings {
		if window_index > 0 && window_string == window_strings[window_index-1] {
			return false
		}
	}
	return true
}
