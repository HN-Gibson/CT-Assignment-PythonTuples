# Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

#created the function to be called and print formatted flight itineraries
def flight_itinerary(list):
    #created a list to be combined later into a formatted string
    itinerary=[]
    for i, (travelers_name,origin,destination) in enumerate(list):
    #formated and appended the variables into the list as a string
        itinerary.append(f"Itinerary {i + 1}: {travelers_name} - From {origin} to {destination}")
    #returned the list joined and formatted as directed    
    return "\n".join(itinerary)
        

#set an example input
flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
#called the function equal to a new variable
formatted_itinerary=flight_itinerary(flights)
#print the formatted itinerary
print(formatted_itinerary)