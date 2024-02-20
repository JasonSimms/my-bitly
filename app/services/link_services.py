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


def generate_click_record(
    recipient_id="none",
):  # TODO can i get more info from the request here?
    try:
        # Get the current date and time
        date_clicked = datetime.datetime.now().isoformat()

        # Create the object with the specified keys
        obj = {
            "recipientId": recipient_id,
            "date_clicked": date_clicked,
        }

        return obj
    except (AttributeError, TypeError) as e:
        # Handle missing or wrong type variables
        print("error raised in except", e)
        return ()
        # raise ValueError("Invalid input: {}".format(e))


def generate_deliverable_links(
    recipient_ids, link_ids, base_url="http://localhost:5000/mylink"
):
    recipient_links = []
    for x in recipient_ids:
        obj = {"recipient": x}
        for y in link_ids:
            print("link", x, y)
            obj[y] = base_url + "mylink/" + y + "?id=" + x
            # recipient_links.append(x+'/'+y)
        recipient_links.append(obj)

    return recipient_links
