// Package to store and process constant values in the program.
package constants

import "log"

// Map variable to store the values for the choices of the Main Menu.
var choice = map[int]string{
	1: "Primes",
	2: "Factors",
	3: "Binary",
	4: "RandomBinary",
	5: "None",
}

// Function to resolve choices in the Main Menu.
func ResolveKey(key int) string {
	value, found_or_not := choice[key]

	if !found_or_not {
		log.Fatalf("Error in Package Constants: Key Invalid")
	}
	return value
}
