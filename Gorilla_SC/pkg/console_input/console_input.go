// Package to deal with console input.
package console_input

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

// Function to take a number input from the console.
func NumberFromCon() int {
	reader := bufio.NewReader(os.Stdin)
	input_str, inp_err := reader.ReadString('\n')
	if inp_err != nil {
		log.Fatalf("Error Code: %v", inp_err)
	}
	input_str = RemoveEOLMarkers(input_str)
	input_str = RemoveWhiteSpaces(input_str)
	input_int, err := strconv.Atoi(input_str)

	if err != nil {
		log.Fatalf("Error Code: %v", err)
	}

	return input_int
}

// Function to remove CLRF characters from a string.
func RemoveEOLMarkers(s string) string {
	s = strings.Replace(s, "\r", "", -1)
	s = strings.Replace(s, "\n", "", -1)

	return s
}

// Function to remove whitespaces from a string.
func RemoveWhiteSpaces(s string) string {
	s = strings.Replace(s, " ", "", -1)

	return s
}
