package routers

import (
	"sample_project/pkg/controllers"

	"github.com/gorilla/mux"
)

var RegisterRoutes = func(router *mux.Router) {
	router.HandleFunc("/", controllers.Index).Methods("GET")
	router.HandleFunc("/api/v1/prime_list", controllers.PrimeList).Methods("GET")
	router.HandleFunc("/api/v1/find_factors", controllers.FindFactors).Methods("GET")
	router.HandleFunc("/api/v1/prime_factors", controllers.FindPrimeFactors).Methods("GET")
	router.HandleFunc("/api/v1/int_to_binary", controllers.IntToBinary).Methods("GET")
	router.HandleFunc("/api/v1/random_binary", controllers.RandomBinary).Methods("GET")
	router.HandleFunc("/api/v1/binary_to_int", controllers.BinToInteger).Methods("GET")
	router.HandleFunc("/api/v1/fibonacci", controllers.FibonacciSequenceController).Methods("GET")
	router.HandleFunc("/api/v1/arith_series", controllers.RegularArithmeticSeriesController).Methods("GET")
	router.HandleFunc("/api/v1/geo_series", controllers.RegularGeometricSeriesController).Methods("GET")
	router.HandleFunc("/api/v1/projectile_path_2d", controllers.ProjectilePath2DController).Methods("GET")
}
