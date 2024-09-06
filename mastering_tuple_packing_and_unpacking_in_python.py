# Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

# Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

# Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.

# - Write a function to iterate over the list of orders. - Unpack each tuple in the list and format the details for display.

def list_orders (list):
    i=1
    formatted_list= []
    for customer_name,product,quantity in list:
        formatted_list.append(f"\nOrder #{i}\nCustomer: {customer_name}\nProduct: {product}\nQuantity: {quantity}\n")
        i+=1
    return "".join(formatted_list)

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

list_of_orders=list_orders(orders)
print(list_of_orders)