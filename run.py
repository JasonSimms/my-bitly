from app import create_app
from dotenv import load_dotenv

# import os

# Load environment variables
# load_dotenv()

# secret = os.getenv("FIREBASE_CREDENTIALS")
# print('hello world, secret:', secret)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
