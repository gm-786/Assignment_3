
from agents import function_tool

@function_tool
def get_flights(destination: str) -> str:
    return f"Flights found to {destination}: PKR 60,000 - 95,000."

@function_tool
def suggest_hotels(destination: str) -> str:
    return f"Hotels in {destination}: Pearl Contiental, Calton, Marriot, Guest Houses."
