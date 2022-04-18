package projectiles

import (
	"errors"
	"math"
	"sample_project/pkg/utils"
)

const g float64 = 9.7803

func CalculateProjectilePath2D(theta float64, u float64, h float64) ([]map[string]float64, error) {
	var x_axis []float64
	var y_axis []float64

	x_u := u * math.Cos((theta * (math.Pi / 180)))
	y_u := u * math.Sin((theta * (math.Pi / 180)))
	time_of_flight := (2 * u * math.Sin(theta*(math.Pi/180))) / g
	x_range := (math.Pow(x_u, 2) * math.Sin(2*(theta*(math.Pi/180)))) / g

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

	for y_coor+h >= 0 || time_value <= time_of_flight || math.Abs(x_coor) <= math.Abs(x_range) {
		x_coor = x_u * time_value
		y_coor = (y_u * time_value) - (g*(math.Pow(time_value, 2)))*0.5
		x_axis = append(x_axis, x_coor)
		y_axis = append(y_axis, y_coor+h)
		time_value += 0.1
	}
	zipped_slices, zip_err := utils.Zipfloat64Slices(x_axis, y_axis)
	if zip_err != nil {
		return nil, errors.New("error zipping slices")
	}
	return zipped_slices, nil
}
