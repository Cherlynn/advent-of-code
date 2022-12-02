package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func part1() {
	input_file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer input_file.Close()
	scanner := bufio.NewScanner(input_file)

	var sum_calorie, max_calorie int = 0, 0
	for scanner.Scan() {
		calorie_text := scanner.Text()
		calorie, err := strconv.Atoi(calorie_text)
		if err == nil {
			sum_calorie += calorie
		} else {
			if sum_calorie > max_calorie {
				max_calorie = sum_calorie
			}
			sum_calorie = 0
		}
	}
	fmt.Println(max_calorie)
}
