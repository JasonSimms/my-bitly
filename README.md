# My Bitly Clone

My Bitly Clone is a RESTful API application that generates short URL links with trackers. It is built using Python and Flask, it will offer a redirect service to intercept traffic on the way to github or my resume.

## Features

[x]- Generate short URLs for any given URL.
[ ]- Generate general tracker for a list of URLS.
[ ]- Redirect traffic onto the URLs
[ ]- Track the number of clicks on each short URL.
[ ]- Provide a RESTful interface for easy integration with other services.

## Deployment

[x]- Connect to firestore
[ ]- Deploy as API

## Usage

### Generate a Short URL

To generate a short URL, make a `POST` request to the `/shorten` endpoint with the original URL in the request body.
