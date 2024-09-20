# Concerts Project

## Overview

This project models a concert system with three main entities: **Band**, **Venue**, and **Concert**. Each band can perform at multiple venues, and each venue can host multiple bands.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Nathanchepkonga/concert_code_challenge.git
   cd concerts

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    venv\Scripts\activate

3. **Install required packages:**
    ```bash
    pip install -r requirements.txt

4. **Initialize Alembic (if needed):**
    ```bash
    alembic init migrations

5. **Create initial migration:**
    ```bash
    alembic revision --autogenerate -m "Initial migration"

6. **Apply migrations:**
    ```bash
    alembic upgrade head

**Running Tests**
To run the tests, ensure your virtual environment is activated and use:
    ```bash
    python -m unittest test_models.py

**Run the Flask Application**
    ```bash
    python app.py








