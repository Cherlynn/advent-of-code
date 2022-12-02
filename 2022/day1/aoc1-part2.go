package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	part1()
	part2()
}

func part2() {
	input_file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer input_file.Close()
	scanner := bufio.NewScanner(input_file)

	var sum_calorie int = 0
	var max_calories [3]int
	for scanner.Scan() {
		calorie_text := scanner.Text()
		calorie, err := strconv.Atoi(calorie_text)
		if err == nil {
			sum_calorie += calorie
		} else {
			for index, value := range max_calories {
				if sum_calorie > value {
					old_max := max_calories[index]
					max_calories[index] = sum_calorie
					sum_calorie = old_max
				}
			}
			sum_calorie = 0
		}
	}
	fmt.Println("Top 3 elves")
	fmt.Println(max_calories[0] + max_calories[1] + max_calories[2])
}
