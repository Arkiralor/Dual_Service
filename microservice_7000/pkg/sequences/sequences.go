package sequences

import (
	"errors"
)

func FibonacciSequence(terms int) ([]int, error) {
	var first, second, counter int = 1, 1, 2
	var fibonacci_sequence []int = []int{first, second}

	if terms < 3 {
		return nil, errors.New("number of terms must be greater than 2")
	}

	for counter <= terms {
		new_element := first + second
		fibonacci_sequence = append(fibonacci_sequence, new_element)
		first = second
		second = new_element
		counter += 1
	}
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
		arith_series = append(arith_series, new_elem)
		counter += 1
	}
	return arith_series, nil
}

func RegularGeometricSeries(start int, terms int, cr int) ([]int, error) {
	var geo_series []int = []int{start}
	var counter int = 1
	if terms < 3 {
		return nil, errors.New("number of terms cannot be lower than 3")
	}
	for counter <= terms {
		last_elem := geo_series[len(geo_series)-1]
		new_elem := last_elem * cr
		geo_series = append(geo_series, new_elem)
		counter += 1
	}
	return geo_series, nil
}
