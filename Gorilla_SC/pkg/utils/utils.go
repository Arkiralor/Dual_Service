package utils

import (
	"errors"
)

func Zipfloat64Slices(slice_01 []float64, slice_02 []float64) ([]map[string]float64, error) {
	var returned_Slice []map[string]float64

	if !(len(slice_01) == len(slice_02)) {
		return nil, errors.New("slices must be of equal length")
	}

	for i := 0; i < len(slice_01); i++ {
		tuple := map[string]float64{
			"x": slice_01[i],
			"y": slice_02[i],
		}
		returned_Slice = append(returned_Slice, tuple)
	}

	return returned_Slice, nil
}
