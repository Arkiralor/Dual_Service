package binaries

import (
	"log"
	"math"
	"math/rand"
	"strconv"
	"time"
)

//Function to convert an decimal integer into its binary equivalent.
func Int64ToBinary(num int) int {
	var num64 = int64(num)
	num_str := strconv.FormatInt(num64, 2)
	num_int, err := strconv.Atoi(num_str)
	if err != nil {
		log.Fatalf("\nError Code: %v\n", err.Error())
	}
	return num_int
}

//Function to convert a binary number into its decimal equivalent.
func BinaryToInt(binary_num int) int {
	var decimal_num int = 0
	var copy_binary_num int = binary_num
	var power int = 0
	for binary_num > 0 {
		remainder := binary_num % 10
		decimal_num += remainder * int(math.Pow(2, float64(power)))
		binary_num /= 10
		power += 1
	}
	log.Printf("Converted %d to %d.\n", copy_binary_num, decimal_num)
	return decimal_num
}

//Function to generate a random binary number, given the number of bits.
//Max. number of bits is 28.
func GenerateRandomBinaryNumber(size int) int {
	var rand_bin, current_size, rand_bit int = 0, 0, 0
	rand.Seed(time.Now().UnixNano())
	for current_size < size {

		rand_bit = rand.Intn(2)
		rand_bin = rand_bin*10 + rand_bit
		current_size += 1
	}
	log.Printf("Random binary number: %d\n", rand_bin)
	return rand_bin
}
