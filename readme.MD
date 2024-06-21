# MongoDB Database Populator

This Python script populates a MongoDB database with user credentials, user information, connections, and user statistics. It connects to a MongoDB instance, creates collections, and inserts predefined data into these collections using Faker for realistic data generation and bcrypt for secure password hashing.

## Prerequisites

- Python 3.x
- `pymongo` library
- `faker` library
- `bcrypt` library

## Installation

1. Clone this repository or download the script files.

2. Install the required libraries if you haven't already:

    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have a MongoDB instance running and accessible.

## Usage

1. Run the `main.py` script:

    ```sh
    python main.py
    ```

2. You will be prompted to enter the database name and MongoDB URI:

    ```sh
    Enter the database name: 
    Enter mongodb uri: 
    ```

3. Follow the prompts to insert the desired number of documents into the `users` collection.

4. The script will then populate the database with the following collections:
    - `users`: Contains user credentials with hashed passwords.
    - `info`: Contains additional information about users.
    - `connections`: Contains user connections data.
    - `user_stats`: Contains user statistics.

## Script Details

### `main.py`

This is the main entry point of the script. It imports necessary functions from modules and executes them in sequence to populate the database.

### Modules

- `modules/connectionsPopulator.py`: Contains the function `create_connections_collection` to populate the connections collection.
- `modules/infoPopulator.py`: Contains the function `populate_info_collection` to populate the user information collection.
- `modules/user_statsPopulator.py`: Contains the function `populate_user_stats_collection` to populate the user statistics collection.
- `modules/usersCollectionPopulator.py`: Contains the function `create_collection` to populate the users collection.

