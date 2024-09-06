# Objective: The aim of this assignment is to deepen your understanding of tuples in Python.

# Task 1: Formatting Flight Itineraries Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should format and return a string that lists each itinerary. For example, if the input is `[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]`, the output should be a string formatted as:

# "Itinerary 1: Alice - From New York to London
#  Itinerary 2: Bob - From Tokyo to San Francisco"

#created the function to be called and print formatted flight itineraries
def flight_itinerary(list):
    #set a default value for the itinerary number
    i=1
    #created a list to be combined later into a formatted string
    itinerary=[]
    #called a loop for each tuple in list and unpacked into variables
    for travelers_name,origin,destination in list:
        #formated and appended the variables into the list as a string
        itinerary.append(f"Itinerary {i}: {travelers_name} - From {origin} to {destination}")
        #increased the value of the itinerary number by 1
        i+=1
    #returned the list joined and formatted as directed    
    return "\n".join(itinerary)
        

#set an example input
flights = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
#called the function equal to a new variable
formatted_itinerary=flight_itinerary(flights)
#print the formatted itinerary
print(formatted_itinerary)