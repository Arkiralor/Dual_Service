package something

import (
	"fmt"
	"os"
	"sample_project/pkg/binaries"
	"sample_project/pkg/console_input"
	"sample_project/pkg/constants"
	"sample_project/pkg/factors"
	"sample_project/pkg/prime_numbers"
)

// Entry point of the program.
func old_ep() {
	fmt.Print(
		"\nWhat is it that you wish to do today?",
		"\n1. Find Prime Numbers",
		"\n2. Find Factors",
		"\n3. Convert to Binary",
		"\n4. Random Binary Number",
		"\n5. Do Nothing",
		"\n\n",
	)
	inp := console_input.NumberFromCon()
	choice := constants.ResolveKey(inp)
	execute_choice(choice)
}

// Function to execute the choice made by the user.
func execute_choice(choice string) {
	if choice == "Primes" {
		locate_primes()
	} else if choice == "Factors" {
		find_factors()
	} else if choice == "Binary" {
		generate_binary()
	} else if choice == "RandomBinary" {
		generate_random_binary()
	} else if choice == "None" {
		os.Exit(1)
	}
}

// Function to execute Choice 01.
func locate_primes() {
	fmt.Printf("\nTill what number do you want to check for primes? ")
	inp := console_input.NumberFromCon()
	list_of_primes := prime_numbers.FindListOfPrimes(inp)

	fmt.Printf("The list of Prime Numbers until %d is:\n%v\n", inp, list_of_primes)
}

func find_factors() {
	fmt.Printf("\nEnter a number to find its factors: ")
	inp := console_input.NumberFromCon()
	list_of_factors := factors.FindFactors(inp)

	fmt.Printf("The list of factors of %d is:\n%v\n", inp, list_of_factors)
}

func generate_binary() {
	fmt.Printf("\nEnter a number to convert to binary: ")
	inp := console_input.NumberFromCon()
	binary_num := binaries.Int64ToBinary(inp)

	fmt.Printf("The binary equivalent of %d is: %d\n", inp, binary_num)
}

func generate_random_binary() {
	fmt.Printf("\nEnter the number of bits to generate a random binary number: ")
	inp := console_input.NumberFromCon()
	binary_num := binaries.GenerateRandomBinaryNumber(inp)

	fmt.Printf("The random binary number is: %d\n", binary_num)
}
