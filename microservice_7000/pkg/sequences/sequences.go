package sequences

import (
	"errors"
	"log"
)

func FibonacciSequence(terms int) ([]int, error) {
	var first, second, counter int = 1, 1, 2
	var fibonacci_sequence []int = []int{first, second}

	if terms < 3 {
		return nil, errors.New("number of terms must be greater than 2")
	}

	for counter <= terms {
		new_element := first + second
		log.Printf("Appending new element to Fibonacci Sequence: %v\n", new_element)
		fibonacci_sequence = append(fibonacci_sequence, new_element)
		first = second
		second = new_element
		counter += 1
	}
	log.Printf("Returning generated Fibonacci Sequence: %v\n", fibonacci_sequence)
	return fibonacci_sequence, nil
}

func RegularArithmeticSeries(start int, terms int, cd int) ([]int, error) {
	var arith_series []int = []int{start}
	var counter int = 1
	if terms < 3 {
		return nil, errors.New("number of terms cannot be lower than 3")
	}
	for counter <= terms {
		last_elem := arith_series[len(arith_series)-1]
		new_elem := last_elem + cd
		log.Printf("Appending new element to Arithmetic Series: %v\n", new_elem)
		arith_series = append(arith_series, new_elem)
		counter += 1
	}
	log.Printf("Returning generated Arithmetic Series: %v\n", arith_series)
	return arith_series, nil
}

func RegularGeometricSeries(start float32, terms float32, cr float32) ([]float32, error) {
	var geo_series []float32 = []float32{start}
	var counter int = 1
	if terms < 3 {
		return nil, errors.New("number of terms cannot be lower than 3")
	}
	for counter <= int(terms) {
		last_elem := geo_series[len(geo_series)-1]
		new_elem := last_elem * cr
		log.Printf("Appending new element to Geometric Series: %v\n", new_elem)
		geo_series = append(geo_series, new_elem)
		counter += 1
	}
	log.Printf("Returning generated Geometric Series: %v\n", geo_series)
	return geo_series, nil
}
