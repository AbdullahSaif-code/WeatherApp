# WeatherApp

WeatherApp is a simple Python application that fetches and processes weather data for a given city using the OpenWeatherMap API. It allows users to search for weather information, save results to a CSV file, and view saved weather data.

## Features

- Fetch current weather data for any city
- Save weather data to a CSV file
- View saved weather data
- Simple menu-driven interface

## Requirements

- Python 3.7+
- Internet connection (for fetching weather data)
- OpenWeatherMap API key

## Installation

1. Clone this repository or download the source code.
2. Install the required Python packages:

   ```sh
   pip install -r requirements.txt
   ```

3. (Optional) Replace the API key in `Main.py` with your own OpenWeatherMap API key.

## Usage

Run the application:

```sh
python Main.py
```

Follow the on-screen menu to search for weather, save data, or open the CSV file.

## File Structure

- `Main.py` - Entry point of the application
- `MenuHandler.py` - Handles user menu and interactions
- `WeatherFetcher.py` - Fetches weather data from the API
- `WeatherProcessor.py` - Processes and formats weather data
- `FileHandler.py` - Handles saving and opening CSV files
- `weather_data.csv` - Stores saved weather data

## License

This project is licensed under the terms of the [CC0 1.0 Universal License](../LICENSE).