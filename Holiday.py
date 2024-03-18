# This is a code that calculates the cost of a mystery holiday.
# Users are told to pick between 1-3 and the code will select the desination with its own pre determined hotel cost
# and plane cost. 
# The desination is then revealed to the user and they can then choose the number of nights,
# and car rental days. The full detailed cost of the holiday is then revealed to them.
city_chosen = lambda city: print(f"The holiday location you will be flying to is {city}!")

# Create a dictionary for options for the user to pick
location = {"1": "spain", "2": "france", "3": "maldives"}

while True:
    destination = input("Pick a number between 1-3 for your mystery holiday: ")

    if destination in location:
        city_flight = location.get(destination)
        city_chosen(city_flight)  # calling function with user's choice
        break  # Exit the loop if the input is valid
    else:
        print("Invalid choice. Please pick a number between 1 and 3.")
        

def hotel_cost(days, city):
    hotel = 0  # Initialize the hotel cost variable
    if city == "spain":
        hotel += int(30)
    elif city == "france":
        hotel += int(60)
    elif city == "maldives":
        hotel += int(500)

    total = hotel * days
    return total

num_nights = int(input("Please enter the number of nights you would like to stay: "))
#print(hotel_cost(num_nights, city_flight))

def plane_cost(city):
    flight_cost = 0
    if city == "spain":
        flight_cost += int(100)
    elif city == "france":
        flight_cost += int(60)
    elif city == "maldives":
        flight_cost += int(1000)
    return flight_cost

#print(plane_cost(city_flight))

rental_days = int(input("Please enter how many days you will like to hire a car: "))

def car_rental(day, city):
    car = 0
    if city == "spain":
        car += int(10)
    elif city == "france":
        car += int(12)
    elif city == "maldives":
        car += int(20)

    total = day * car
    return total


#print(car_rental(rental_days, city_flight))

def holiday_cost():
    total = hotel_cost(num_nights, city_flight) + plane_cost(city_flight) + car_rental(rental_days, city_flight)
    return total 
total_cost = holiday_cost()

print(f"The toal cost of your holiday to {city_flight} is £ {total_cost}")
print("Please find the cost breakdown below: ")
print(f"The cost of the hotel is £ {hotel_cost(num_nights, city_flight)} ")
print(f"The cost of the plane is £ {plane_cost(city_flight)}")
print(f"The cost of the car rental is £ {car_rental(rental_days, city_flight)}")
