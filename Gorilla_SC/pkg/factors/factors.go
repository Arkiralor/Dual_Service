package factors

import (
	"log"
	"sort"
)

func FindFactors(num int) []int {
	var factors []int = []int{1}
	var upper_limit int = num / 2

	for i := 2; i <= upper_limit; i += 1 {
		if num%i == 0 {
			log.Printf("Factor found: %v\n", i)
			factors = append(factors, i)
		}
	}
	factors = append(factors, num)
	sort.Ints(factors)
	return factors
}
