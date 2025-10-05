# Import the tools we need to work with the webpage
from pyscript import document, display

# Store our business name in a variable
business_name = "CLOCK THAT TEA"

def process_order(e):
    """
    This function runs when the 'Place Order' button is clicked.
    It calculates the total price and shows the order summary.
    e: Event object (required by PyScript but we don't use it here)
    """
    
    # First, clear any previous order summary
    document.getElementById("orderOutput").innerHTML = ""
    
    # Start with total at 0
    total = 0
    
    # Check each checkbox and add its price to the total if checked
    # tea1 is Earl Grey (350 pesos)
    if document.getElementById("tea1").checked:
        total += int(document.getElementById("tea1").value)
    
    # tea2 is Jasmine Green Tea (250 pesos)
    if document.getElementById("tea2").checked:
        total += int(document.getElementById("tea2").value)
    
    # tea3 is English Breakfast (300 pesos)
    if document.getElementById("tea3").checked:
        total += int(document.getElementById("tea3").value)
    
    # tea4 is Chamomile (200 pesos)
    if document.getElementById("tea4").checked:
        total += int(document.getElementById("tea4").value)
    
    # tea5 is Matcha Latte (450 pesos)
    if document.getElementById("tea5").checked:
        total += int(document.getElementById("tea5").value)
    
    # Get the customer information from the form
    # .strip() removes extra spaces from the beginning and end
    customer_name = document.getElementById("customerName").value.strip()
    customer_address = document.getElementById("customerAddress").value.strip()
    customer_phone = document.getElementById("customerPhone").value.strip()
    
    # Check if customer filled in all the required fields
    if not customer_name or not customer_address or not customer_phone:
        display("Please complete all fields before placing your order.", target="orderOutput")
        return
    
    # Check if phone number is valid (only numbers and at least 10 digits long)
    if not customer_phone.isdigit() or len(customer_phone) < 10:
        display("Please enter a valid phone number (at least 10 digits).", target="orderOutput")
        return
    
    # Check if customer selected at least one tea
    if total == 0:
        display("Please select at least one tea to order.", target="orderOutput")
        return
    
    # Create the order summary message
    # Using triple quotes for multi-line text
    order_summary = f"""
✅ Order Confirmed!
-------------------------
Customer Name: {customer_name}
Delivery Address: {customer_address}
Contact Number: {customer_phone}
-------------------------
Total Amount: ₱{total}
-------------------------
Your tea order is being processed. Thank you for choosing {business_name}!
"""
    
    # Display the order summary in the output area
    display(order_summary, target="orderOutput")