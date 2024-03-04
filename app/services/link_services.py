# link_generator.py
# from ..models import UserLink
import datetime


############################ Deprecated? ############################
def generate_user_link(name, url, creator):
    if not name or not url:
        raise ValueError("Name and URL are required.")
    try:
        # Generate an ID
        id = f"link_{datetime.datetime.now().isoformat()}"

        # created_at = datetime.datetime.now().isoformat()
        # updated_at = datetime.datetime.now().isoformat()

        user_link = {
            "id": id,
            "url": url,
            "nickname": name,
            "creator": creator,
            # "createdAt": created_at,
            # "updatedAt": updated_at
        }

        #   # Create a new UserLink object with the provided url and nickname, and default values for id, createdAt, and updatedAt.
        # user_link = UserLink(
        #     id=id,
        #     url=url,
        #     nickname=name,
        #     createdAt=created_at,
        #     updatedAt=updated_at
        # )

        return user_link
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
