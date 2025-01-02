# Django Project for Hotel Data Transformation

This Django project leverages the Gemini Flash 2.0 model to enhance hotel data by generating unique titles, descriptions, summaries, reviews, and ratings. It integrates with a Dockerized PostgreSQL database, shared with a Scrapy project.
---
## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Install Dependencies](#2-install-dependencies)
- [Running the Application](#running-the-application)
  - [1. Start the Services](#1-start-the-services)
  - [2. Apply Migrations](#2-apply-migrations)
  - [3. Generate Content](#3-generate-content)
  - [4. Create a Superuser](#4-create-a-superuser)
- [Testing](#testing)
- [Summary](#summary)

---
## Features
This Django project provides the following functionalities:

1. **Fetch Hotel Data:**
   - Retrieve data from the `hotels` table in the shared PostgreSQL database.

2. **Generate Unique Titles and Descriptions:**
   - Generate unique titles using the Gemini Flash 2.0 model.
   - Create descriptions based on the title, city name, and room type.
   - Store the results in the `generated_title_desc` table with the following columns:
     - `hotel_id`
     - `title`
     - `generated_title`
     - `description`

3. **Generate Summaries and Reviews:**
   - Generate summaries using the title, city name, price, rating, room type, and location.
   - Generate a rating (between 1 and 5) and a short review based on price, rating, and room type.
   - Store the results in the `summary_table` with the following columns:
     - `hotel_id`
     - `summary`
     - `rating`
     - `review`

4. **Database Interaction:**
   - Seamless integration with the Dockerized PostgreSQL database.
   - All new tables are created and managed within the same database.

---
## Prerequisites
- Docker
- Git
- Python 3.11 or higher (for local development)
- **Important:** The [Scrapy](https://github.com/Muntasir-Ayan/scrapy-trip-dot-com) project must be running. This Django project shares the same database with the Scrapy project. Clone and run the Scrapy repository first:
  ```bash
  git clone https://github.com/Muntasir-Ayan/scrapy-trip-dot-com.git
  cd scrapy-trip-dot-com
  docker-compose up --build
  ```

---
## Environment Setup

### 1. Clone the Repository
Clone this Django project:
```bash
git clone https://github.com/Muntasir-Ayan/llm_project.git
cd llm_project
```

### 2. Install Dependencies
Set up a virtual environment and install the required Python libraries:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---
## Running the Application

### 1. Start the Services
Build and start the Docker containers:
```bash
docker-compose up --build
```

### 2. Apply Migrations
In a new terminal, run the following commands:
```bash
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```

### 3. Generate Content
Run the content generation command to populate the database:
```bash
docker exec -it django-app python manage.py generate_content
```

### 4. Create a Superuser
To access the database via the Django admin panel, create a superuser:
```bash
docker exec -it django-app bash
python manage.py createsuperuser
```

Access the Django admin panel at [http://localhost:8000/admin](http://localhost:8000/admin) and check the database table.

---
## Testing
Run the test suite with coverage:
```bash
docker exec -it django-app bash
pytest --cov=hotel_data
```


---
## Summary
This project automates hotel data transformation using AI-powered tools, integrates seamlessly with Dockerized services, and provides robust testing and database management features. Follow the steps above to set up and run the application. For any issues, consult the documentation or contact the project maintainers.
