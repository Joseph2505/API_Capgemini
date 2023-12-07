# FastAPI MongoDB REST API

## Introduction

This project is a RESTful API built using FastAPI for creating, reading, updating, and deleting data in a MongoDB database. It provides an interface to interact with stock information.

This API project is part of the Big Data Applications course given by Capgemini. The development team consists of Eva CHAMBARON, Rahamim SITBON, and Joseph XU.

## Setup Environment

1. Create a virtual environment using [virtualenv](https://pypi.org/project/virtualenv/):

    ```bash
    virtualenv venv
    ```

2. Activate the virtual environment:

    - For Linux/Mac:

        ```bash
        source venv/bin/activate
        ```

    - For Windows:

        ```bash
        source venv/Scripts/activate
        ```

## Install Dependencies

Install the required packages using pip (You can find all dependencies in our requirements.txt file):

```bash
pip install fastapi pymongo uvicorn
```
## Start the Server

Run the FastAPI application using uvicorn:

```bash
uvicorn index:app --reload
```
The --reload option enables automatic reloading of the server on code changes, making development easier.

## API Endpoints
```bash
GET /{siret}: Retrieve information for a specific stock based on its SIRET number.
```
```bash
DELETE /{siret}: Delete a stock entry based on its SIRET number.
```
## Usage
Access the API documentation at http://127.0.0.1:8000/docs for interactive documentation.

Use http://127.0.0.1:8000/redoc for a more structured API documentation.