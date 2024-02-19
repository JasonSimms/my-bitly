# link_generator.py
import datetime


def generate_link(name, url):
    print("im here", "name: ", name, "  url: ", url)
    if not name or not url:
        raise ValueError("Name and URL are required.")
    try:
        # Generate an ID
        id = name.strip().lower().replace(" ", "")

        # Trim and lowercase the name and url
        url = url.strip().lower()

        # Get the current date and time
        date_generated = datetime.datetime.now().isoformat()

        # Create the object with the specified keys
        obj = {
            "id": id,
            "name": name,
            "url": url,
            "dateGenerated": date_generated,
            "clicks": [],
        }

        return obj
    except (AttributeError, TypeError) as e:
        # Handle missing or wrong type variables
        print("error raised in except", e)
        return ()
        # raise ValueError("Invalid input: {}".format(e))
