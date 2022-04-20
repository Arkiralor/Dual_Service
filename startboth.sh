cd Gorilla_SC/cmd/main
echo "Building Gorilla_SC/cmd/main"
go build
echo "Built Gorilla_SC/cmd/main"
echo "Starting Gorilla_SC/cmd/main"
echo "Gorilla APIs active..."
go run main.go &
cd ../../../Django_SC/
python manage.py runserver