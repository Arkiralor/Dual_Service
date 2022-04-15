package controllers

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"sample_project/pkg/binaries"
	"sample_project/pkg/factors"
	"sample_project/pkg/prime_numbers"
	"strconv"
)

func Index(w http.ResponseWriter, r *http.Request) {
	inp := r.URL.Query().Get("inp")
	log.Println(inp)

	resp := map[string]string{
		"message": inp,
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

func PrimeList(w http.ResponseWriter, r *http.Request) {
	upper_limit_str := r.URL.Query().Get("upper_limit")
	upper_limit, err := strconv.ParseInt(upper_limit_str, 10, 0)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}

	prime_list := prime_numbers.FindListOfPrimes(int(upper_limit))

	var resp map[string]interface{} = map[string]interface{}{
		"function": fmt.Sprintf("Find the list of all Prime Numbers <= '%v'.", upper_limit),
		"query":    upper_limit,
		"result":   prime_list,
		"length":   len(prime_list),
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

func FindFactors(w http.ResponseWriter, r *http.Request) {
	num_str := r.URL.Query().Get("num")
	num, err := strconv.Atoi(num_str)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}
	factor_list := factors.FindFactors(num)
	var resp map[string]interface{} = map[string]interface{}{
		"function": fmt.Sprintf("Find the list of all Factors of '%v'.", num),
		"query":    num,
		"result":   factor_list,
		"length":   len(factor_list),
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

// View to find all prime factors of 'num' in GET request.
func FindPrimeFactors(response_writer http.ResponseWriter, request *http.Request) {
	var prime_factors []int
	num_str := request.URL.Query().Get("num")
	num, err := strconv.ParseInt(num_str, 10, 0)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}
	factor_list := factors.FindFactors(int(num))
	for i := 0; i < len(factor_list); i++ {
		if prime_numbers.CheckIfPrime(factor_list[i]) {
			log.Println("Prime factor found: ", factor_list[i])
			prime_factors = append(prime_factors, factor_list[i]) //Filtering non-prime factors
		}
	}
	prime_factors = prime_factors[1:] //Removing '1' as 1 is a co-prime of all numbers.
	var resp map[string]interface{} = map[string]interface{}{
		"function": fmt.Sprintf("Find Prime Factors of %v.", num),
		"query":    num,
		"result":   prime_factors,
		"length":   len(prime_factors),
	}
	response_writer.Header().Set("Content-Type", "application/json")
	response_writer.WriteHeader(http.StatusOK)
	log.Printf("Returning response: %v", resp["result"])
	json.NewEncoder(response_writer).Encode(resp)
}

func IntToBinary(w http.ResponseWriter, r *http.Request) {
	num_str := r.URL.Query().Get("num")
	num, err := strconv.ParseInt(num_str, 10, 0)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}
	binary_number := binaries.Int64ToBinary(int(num))
	var resp map[string]interface{} = map[string]interface{}{
		"function": fmt.Sprintf("Convert '%v' in decimal to '%v' in binary.", num, num),
		"query":    num,
		"result":   binary_number,
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

func BinToInteger(w http.ResponseWriter, r *http.Request) {
	binary_number_str := r.URL.Query().Get("binary_number")
	binary_number, err := strconv.ParseInt(binary_number_str, 10, 0)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}
	integer_number := binaries.BinaryToInt(int(binary_number))

	var resp = map[string]interface{}{
		"function": fmt.Sprintf("Convert '%v' in binary to '%v' in decimal.", binary_number_str, integer_number),
		"query":    binary_number_str,
		"result":   integer_number,
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}

func RandomBinary(w http.ResponseWriter, r *http.Request) {
	bits_str := r.URL.Query().Get("bits")
	bits, err := strconv.ParseInt(bits_str, 10, 0)
	if err != nil {
		log.Printf("Error: %v", err.Error())
		panic(err)
	}
	binary_number := binaries.GenerateRandomBinaryNumber(int(bits))
	var resp = map[string]interface{}{
		"function": fmt.Sprintf("Generate a random binary number of '%v' bits.", bits),
		"query":    int(bits),
		"result":   binary_number,
		"length":   int(bits),
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}
