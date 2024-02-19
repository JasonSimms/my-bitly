# link_generator.py
import datetime


def generate_link(name, url):

    # Get the current date and time
    date_generated = datetime.datetime.now().isoformat()

    # Create the object with the specified keys
    obj = {
        # "id": id,
        "name": name,
        "url": url,
        "dateGenerated": date_generated,
    }

    return obj
