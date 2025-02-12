import random

def get_mock_weather(city):
    mock_data = {
        "temperature": round(random.uniform(15, 35), 1),
        "humidity": random.randint(30, 90),
        "description": random.choice(["Sunny", "Cloudy", "Rainy", "Windy", "Stormy"])
    }
    return mock_data

def main():
    city = input("Enter city name: ")
    weather = get_mock_weather(city)
    print(f"Weather in {city}:")
    print(f"Temperature: {weather['temperature']}°C")
    print(f"Humidity: {weather['humidity']}%")
    print(f"Description: {weather['description']}")

if __name__ == "__main__":
    main()
