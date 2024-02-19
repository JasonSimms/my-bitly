# My Bitly Clone

My Bitly Clone is a RESTful API application that generates short URL links with trackers. It is built using Python and Flask, it will offer a redirect service to intercept traffic on the way to github or my resume.

## Features

- Generate a redirect service.
- Enter recipients and create tracker tags.
- Apply the tags dynamically as params to URL of projects
- Redirect traffic to the destination and log the activity
- BONUS ROUND 1 - Generate an admin front End
- BONUS ROUND 2 -- Generate PDF's dynamically providing the URL's
- BONUS ROUND 3 --- Generate Emails dynamically with URLs 


## Steps

- [x] Connect to firestore
- [ ] Code API logic
- [ ] Add unittesting
- [ ] Deploy as API
- [ ] Deploy Front End

## Usage

NOT READY


### Generate a Short URL

To generate a short URL, make a `POST` request to the `/shorten` endpoint with the original URL in the request body.
