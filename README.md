# Orchestra Configuration Engine

This project is a basic configuration engine for managing custom fields on HubSpot's Deal object and email cadences in Upso. It allows Balco portfolio companies to add and modify custom fields, as well as manage email cadences. The implementation is done using FastAPI and SQLAlchemy, and it includes mock functions to simulate API calls to HubSpot and Upso.

## Project Structure

```plaintext
|   Balio_task.docx
|   .gitignore
|   main.py
|
+---api
|   |   mock_functions.py
|   |
|
+---config
|   |   database.py
|   |
|
+---data
|       High-Level Architecture Diagram.png
|       Infrastructure Diagram.png
|       Simplified Design for Low Scale.png
|       test.db
|
+---models
|   |   schemas.py
|   |
```

### Description of Key Files

- **Balio_task.docx**: Documentation of the task requirements and answers.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **main.py**: Entry point of the application.
- **test.db**: SQLite database file.

#### `api`
- **mock_functions.py**: Contains mock functions to simulate API calls to HubSpot and Upso.

#### `config`
- **database.py**: Manages database connection and schema.

#### `data`
- **High-Level Architecture Diagram.png**: High-level architecture diagram of the project.
- **Infrastructure Diagram.png**: Diagram of the project infrastructure.
- **Simplified Design for Low Scale.png**: Diagram of the simplified design for low-scale environments.
- **test.db**: Another reference to the SQLite database file.

#### `models`
- **schemas.py**: Defines Pydantic models for request validation.

## Setup

### Create venv
In windows, please set `ExecutionPolicy`:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Now we need to create a venv and activate it:
```bash
python -m venv .balio
.\.balio\Scripts\activate
git clone https://github.com/egenc/balio-case-study
```

### Install Dependencies
Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Run the Application
Start the FastAPI application using Uvicorn:

```bash
uvicorn main:app --reload
```
Output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [29704] using StatReload
INFO:     Started server process [31736]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


### Access the API Documentation
Open your browser and go to:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

Now, please open a separate cmd console.

### Root Endpoint
- **GET /**: Displays a welcome message.

### Custom Fields
- **Add Custom Field**: `POST /add_custom_field/`

```json
{
  "field_name": "key_contact",
  "field_type": "text",
  "field_value": "John Doe"
}
```
Example1:
```bash
curl -X POST "http://127.0.0.1:8000/add_custom_field/" -H "Content-Type: application/json" -d "{\"field_name\": \"key_contact\", \"field_type\": \"text\", \"field_value\": \"John Doe\"}"
```

Example2:
```bash
curl -X POST "http://127.0.0.1:8000/add_custom_field/" -H "Content-Type: application/json" -d "{\"field_name\": \"company_growth_rate\", \"field_type\": \"number\", \"field_value\": \"10%\"}"
```

- **Modify Custom Field**: `PUT /modify_custom_field/{field_id}`

```json
{
  "field_name": "primary_contact"
}
```
Example:
```bash
curl -X PUT "http://127.0.0.1:8000/modify_custom_field/1" -H "Content-Type: application/json" -d "{\"field_name\": \"primary_contact\"}"
```



### Email Cadences
- **Add Email Cadence**: `POST /add_email_cadence/`

```json
{
  "cadence_name": "Weekly Outreach",
  "timing": "Every Monday",
  "template": "Hello, this is a weekly update..."
}
```

Example1:
```bash
curl -X POST "http://127.0.0.1:8000/add_email_cadence/" -H "Content-Type: application/json" -d "{\"cadence_name\": \"Weekly Outreach\", \"timing\": \"Every Monday\", \"template\": \"Hello, this is a weekly update...\"}"
```
Example2:
```bash
curl -X POST "http://127.0.0.1:8000/add_email_cadence/" -H "Content-Type: application/json" -d "{\"cadence_name\": \"Monthly Outreach\", \"timing\": \"First Monday of every month\", \"template\": \"Hello, this is a monthly update!!!\"}"

```
- **Modify Email Cadence**: `PUT /modify_email_cadence/{cadence_id}`

```json
{
  "timing": "Every Tuesday",
  "template": "Hello, this is an updated weekly email..."
}
```
Example:
```bash
curl -X PUT "http://127.0.0.1:8000/modify_email_cadence/1" -H "Content-Type: application/json" -d "{\"timing\": \"Every Tuesday\", \"template\": \"Hello, this is an updated weekly email...\"}"
```

## How to View the Database
You can view the contents of the database using various methods such as:

- **DB Browser for SQLite**: Open the `test.db` file.
- **SQLAlchemy Queries**: Use a script to query and print the database contents.
- **API Endpoints**: Access custom fields and email cadences through specific API endpoints.

However, easiest way to view it is to use this link:
https://inloop.github.io/sqlite-viewer/
Drag and drop the `test.db` file to the system and you can view tables and content with minimum effort.

:umbrella: OR simply run:
```bash
python config/view_database.py
```

:warning: **Please don't forget to run the code before viewing it. Running the code will create the database under `data/` folder with the name `test.db`**

## Database Schema
The database is set up using SQLAlchemy. The schema includes two main tables:

- **CustomField**:
  - `id`: Integer, Primary Key
  - `field_name`: String
  - `field_type`: String
  - `field_value`: Text

- **EmailCadence**:
  - `id`: Integer, Primary Key
  - `cadence_name`: String
  - `timing`: String
  - `template`: Text

## Mock Functions
The project includes mock functions to simulate API calls to HubSpot and Upso. These are located in `api/mock_functions.py`.

## Testing
The project structure includes a `tests` directory with unit tests for managing custom fields and email cadences.
Simply run:
```bash
python -m pytest tests/
```