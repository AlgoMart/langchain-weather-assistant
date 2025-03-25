# langchain-weather-assistant

This project demonstrates how to create a weather agent using LangChain, OpenAI's GPT-4, and external APIs to fetch weather data based on a user's query. It integrates with OpenWeatherMap to retrieve weather details and geolocation information (latitude and longitude) for a given city. The app is built using Streamlit for the user interface.

## Features

-   **Weather Information Retrieval:** Fetch current weather details (e.g., temperature, humidity, etc.) based on latitude and longitude.
-   **Geolocation Lookup:** Convert a city name to latitude and longitude using OpenWeatherMap's API.
-   **Streamlit Interface:** A simple web interface where users can input a city name and get weather details.
-   **LangChain Agent:** Utilizes LangChain to build a natural language processing agent powered by GPT-4 to process and invoke the weather and geolocation tools.

## Requirements

-   `requests`
-   `streamlit`
-   `langchain`
-   `langchain_openai`
-   `python-dotenv`

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## Setup

1. **Sign up for an API Key from OpenWeatherMap**:

    - Go to [OpenWeatherMap](https://openweathermap.org/api) and sign up to get an API key.
    - Save your API key in the `.env` file as `WEATHER_API_KEY` (example `.env` content):
        ```
        WEATHER_API_KEY=your_api_key_here
        ```

2. **Clone this Repository**:

    ```bash
    git clone https://github.com/your-username/weather-agent-langchain.git
    cd weather-agent-langchain
    ```

3. **Run the Streamlit App**:

    To start the app, run:

    ```bash
    streamlit run app.py
    ```

    This will open the app in your browser.

## How It Works

1. **LangChain Agent**: The agent is initialized with two structured tools:

    - `get_latitude_longitude`: Fetches latitude and longitude for a city name using OpenWeatherMap's geolocation API.
    - `get_weather`: Fetches weather details (like temperature and humidity) for the given latitude and longitude using OpenWeatherMap's weather API.

2. **Interaction Flow**:

    - The user inputs a city name in the Streamlit app.
    - The LangChain agent processes the query, first converting the city name to latitude and longitude, then retrieving the corresponding weather details.
    - The weather details are then displayed in the app's UI.

3. **User Query**: The user can ask any weather-related query, and the agent will interpret the input, call the appropriate tool(s), and return the relevant data.

## Example Usage

1. Enter a city name like "New York" in the text input field.
2. Click "Get Weather" to retrieve weather details such as temperature, humidity, and weather conditions for that city.

## Code Explanation

-   **`WeatherModel` and `LatitudeLongitudeModel`**: These are Pydantic models used to define the input schema for the weather and geolocation tools.
-   **`get_weather` and `get_latitude_longitude`**: Functions that make HTTP requests to the OpenWeatherMap API to fetch weather details and geolocation data.
-   **LangChain Tools**: The tools are wrapped using `StructuredTool` to match the required function signature and description for LangChain's agent.
-   **Streamlit UI**: A simple UI to allow users to input a query and view the results.

## Weather Assistant Images

#### Screen as soon as application starts

![Screen as soon as application starts](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*eMcv9WZHqqboIXkQVbqnCg.png)

### Screen as soon as you enter your question and press Get Weather

![Screen as soon as you enter your question and press Get Weather](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*FIdPnzFJXHOWP0KMMIwDdg.png)

### Screen with LLM response

![Screen with LLM response](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sgkviCs4guwHolgGlBvR-g.png)

### Screen comparing weather in Pune and Bangalore

![Screen comparing weather in Pune and Bangalore](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UFEnVpHhVjA4I4Fkc_31zg.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, feel free to open an issue on the GitHub repository or contact [your-email@example.com].

---

You can modify the repository URL and email as necessary!
