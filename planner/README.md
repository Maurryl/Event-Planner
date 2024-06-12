# Event Planner CLI Application

## Description

A Python CLI application to manage events, guests, and venues using SQLAlchemy ORM.

## Features

- Create, delete, view, and find events.
- Manage guests and assign them to events.
- Manage venues and link them to events.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install dependencies:
    ```bash
    pipenv install
    ```
4. Initialize the database:
    ```bash
    pipenv run python -c 'from models.base import Base, engine; Base.metadata.create_all(engine)'
    ```
5. Run the application:
    ```bash
    pipenv run python cli/main.py
    ```

## Usage

Follow the CLI menus to manage events, guests, and venues.

## License

This project is licensed under the MIT License.
