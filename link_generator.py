# link_generator.py
import datetime
import socket
import uuid


def generate_link(name):
    # Generate an ID
    id = str(uuid.uuid4())

    # Get the current date and time
    date_generated = datetime.datetime.now().isoformat()

    # Initialize datesClicked as an empty list
    dates_clicked = []

    # Get the IP address of the machine
    ip = socket.gethostbyname(socket.gethostname())

    # Generate a URL based on the name
    base_url = "base_url/"  # Replace with your base URL TODO replace with deployed host
    url = base_url + name

    # Create the object with the specified keys
    obj = {
        "id": id,
        "name": name,
        "dateGenerated": date_generated,
        "datesClicked": dates_clicked,
        "ip": ip,
        "url": url,
    }

    return obj
