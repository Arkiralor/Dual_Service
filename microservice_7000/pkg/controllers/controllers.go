package controllers

import (
	"encoding/json"
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
		"function":      "Find the list of all Prime Numbers <= 'n'.",
		"input":         upper_limit,
		"prime_numbers": prime_list,
		"length":        len(prime_list),
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
		"function": "Find the list of all Factors of 'n'.",
		"input":    num,
		"factors":  factor_list,
		"length":   len(factor_list),
	}

	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
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
		"function":      "Convert 'n' in decimal to 'n' in binary.",
		"input":         num,
		"binary_number": binary_number,
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
		"function":      "Generate a random binary number of 'n' bits.",
		"input":         int(bits),
		"binary_number": binary_number,
		"length":        int(bits),
	}
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(resp)
}
