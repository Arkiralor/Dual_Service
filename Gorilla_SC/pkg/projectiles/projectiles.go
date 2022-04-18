package projectiles

import (
	"errors"
	"log"
	"math"
	"sample_project/pkg/utils"
)

const g float64 = 9.7803

func ConvertDegToRadian(angle float64) float64 {
	return angle * (math.Pi / 180)
}

func CalculateProjectilePath2D(theta float64, u float64, h float64) ([]map[string]float64, error) {
	var x_axis []float64
	var y_axis []float64

	log.Println("Converting Degree value to Radian...")
	theta = ConvertDegToRadian(theta)

	log.Println("Splitting initial launch velocity into X and Y components...")
	x_u := u * math.Cos(theta)
	y_u := u * math.Sin(theta)
	log.Println("Calculating total time of flight...")
	x_range := (math.Pow(x_u, 2) * math.Sin(2*theta)) / g

	var time_value float64 = 0
	var x_coor float64 = 0
	var y_coor float64 = 0

	if theta < 0 {
		return nil, errors.New("angle of projection must be greater than 0")
	}
	if u < 0 {
		return nil, errors.New("speed of projectile must be greater than 0")
	}
	if h < 0 {
		return nil, errors.New("height of projectile must be greater than or equal to 0")
	}

	for y_coor+h >= 0 || math.Abs(x_coor) <= math.Abs(x_range) {
		x_coor = x_u * time_value
		y_coor = (y_u * time_value) - (g*(math.Pow(time_value, 2)))*0.5
		log.Printf("X-coordinate for t = %v is %v\n", math.Round(time_value*100)/100, math.Round(x_coor*100)/100)
		x_axis = append(x_axis, math.Round(x_coor*100)/100)
		log.Printf("Y-coordinate for t = %v is %v\n", math.Round(time_value*100)/100, math.Round((y_coor+h)*100)/100)
		y_axis = append(y_axis, math.Round((y_coor+h)*100)/100)
		time_value += 0.1
	}

	log.Println("Zipping slice of X and Y coordinate...")
	zipped_slice, zip_err := utils.Zipfloat64Slices(x_axis, y_axis)
	if zip_err != nil {
		return nil, errors.New("error zipping slices")
	}

	log.Printf("Returning zipped slice: %v...\n", zipped_slice[:10])

	return zipped_slice, nil
}
