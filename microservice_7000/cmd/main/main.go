package main

import (
	"log"
	"net/http"
	"sample_project/pkg/routers"

	"github.com/gorilla/mux"
)

func main() {
	router := mux.NewRouter()
	routers.RegisterRoutes(router)
	http.Handle("/", router)
	log.Fatal(http.ListenAndServe("localhost:7000", router))
}
