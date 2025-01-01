# Hotel Content Generator Using LLM

Using Gemini this Django project will generate new hotel Title, description from (title, city_name, room_type), review (price, rating, room_type), rating( generate a rating between 1 to 5), and summarry from (title, city_name, price, rating,room_type, location).

## Prerequisites
- Docker
- Git
- Python 3.11 or higher (for local development)
- **Important**: [Scrapy](https://github.com/Muntasir-Ayan/scrapy-trip-dot-com) Project should be running, This two project sharing same database on docker. 

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd ollama-prop-rewriter
```

### 2. Install Dependencies
Create a virtual environment and install the required Python libraries:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Application

### 1. Starting the Services
Build and start the containers:
```bash
docker-compose up --build 
```

### 2. Migration and Migrate
Go to new terminal:
```bash
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```
Generate:
```bash
docker exec -it django-app python manage.py generate_content
```
Create Super User to Check database in Django Admin:
```bash
docker exec -it django-app bash
python manage.py createsuperuser
```
### Testing 
```bash
docker exec -it django-app bash
pytest --cov=hotel_data
```
