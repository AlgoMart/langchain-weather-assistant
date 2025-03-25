import os

import requests
import streamlit as st
from dotenv import load_dotenv
from langchain.agents import AgentType, initialize_agent
from langchain.tools import StructuredTool
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

load_dotenv()


# Define structured input schema for the tools
class WeatherModel(BaseModel):
    latitude: float
    longitude: float


class LatitudeLongitudeModel(BaseModel):
    city_name: str


# Tool function to fetch weather details
def get_weather(latitude: float, longitude: float) -> dict:
    API_KEY = os.getenv("WEATHER_API_KEY")
    API_URL = (
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric"
    )
    response = requests.get(API_URL)
    return response.json()


# Tool function to fetch latitude and longitude
def get_latitude_longitude(city_name: str) -> list:
    API_KEY = os.getenv("WEATHER_API_KEY")
    API_URL = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=3&appid={API_KEY}"
    response = requests.get(API_URL)
    return response.json()


# Create structured tools using StructuredTool
weather_tool = StructuredTool.from_function(
    func=get_weather,
    name="get_weather",
    description="Fetch the weather details for given latitude and longitude.",
    args_schema=WeatherModel,
)

latitude_longitude_tool = StructuredTool.from_function(
    func=get_latitude_longitude,
    name="get_latitude_longitude",
    description="Fetch the latitude and longitude for a city name.",
    args_schema=LatitudeLongitudeModel,
)

# Initialize LangChain Agent
llm = ChatOpenAI(model="gpt-4-turbo", temperature=0)

agent = initialize_agent(
    tools=[latitude_longitude_tool, weather_tool],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    # verbose=True,
)

# Streamlit App UI
st.title("🌤️ Weather Agent using LangChain")

user_query = st.text_input("Enter your query about the weather:")

if st.button("Get Weather"):
    with st.spinner("Fetching weather details..."):
        response = agent.invoke({"input": user_query})

        st.subheader("🌐 Agent Response")
        st.write(response["output"])
