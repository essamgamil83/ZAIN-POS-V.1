# Zain ERP Backend

This directory contains the backend code for the Zain ERP project, built with Django and Django REST Framework.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up environment variables:**
    - Create a `.env` file by copying the `.env.example` file:
      ```bash
      cp .env.example .env
      ```
    - Edit the `.env` file and provide the necessary values for your environment.

3.  **Configure the database:**
    - Make sure you have PostgreSQL installed and running.
    - Create a database and a user with the credentials specified in your `.env` file.

4.  **Run database migrations:**
    ```bash
    python manage.py migrate
    ```

4.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
