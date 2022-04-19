FROM golang:1.17

WORKDIR /Gorilla_SC

COPY . .

RUN go get github.com/gorilla/mux

CMD ["go", "run", "cmd/main/main.go", "0.0.0.0:7000"]