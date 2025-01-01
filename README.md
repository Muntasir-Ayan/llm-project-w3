# Hotel Content Generator Using LLM

Using Gemini this Django project will generate new hotel Title, description from (title, city_name, room_type), review (price, rating, room_type), rating( generate a rating between 1 to 5), and summarry from (title, city_name, price, rating,room_type, location).

## Prerequisites
- Docker
- Git
- Python 3.11 or higher (for local development)
- **Important**: [Scrapy](https://github.com/Muntasir-Ayan/scrapy-trip-dot-com) Project should be running, This two project sharing same database on docker. 

## Environment Setup

### Clone the Repository
```bash
git clone <repository-url>
cd ollama-prop-rewriter
```

### Create a `.env` File
Create a `.env` file in the root directory with the following content:
```
DB_USERNAME=aa_nadim
DB_PASSWORD=aa_nadim123
DB_NAME=scraping_db
DB_PORT=5432
DB_HOST=postgres
OLLAMA_BASE_URL=http://ollama:11434/api/generate
SECRET_KEY='django-insecure-nc4($e*vaa^7ftbpg^5y8yz-5a(-n18-*#ln^wpbtw5a0-@e5('
```

## Running the Application

### Starting the Services
Build and start the containers:
```bash
docker-compose up --build ollama
docker-compose ps
docker-compose up --build django_app
docker-compose ps
```

### Ollama Service Management
Enter the Ollama service:
```bash
docker-compose exec ollama bash
```
List available models:
```bash
ollama list
```
Remove a specific model:
```bash
ollama rm gemma2:2b
```
Pull a specific model:
```bash
docker-compose exec ollama ollama pull llama3.2:1b
```

### Run Content Generation Commands
Each command processes hotels in batches. Adjust the batch size using the `--batch-size` parameter.

#### Rewrite Hotel Titles
```bash
docker-compose exec django_app python manage.py rewrite_titles --batch-size 2
```

#### Generate Hotel Descriptions
```bash
docker-compose exec django_app python manage.py generate_descriptions --batch-size 2
```

#### Generate Hotel Summaries
```bash
docker-compose exec django_app python manage.py generate_summaries --batch-size 2
```

#### Generate Hotel Reviews
```bash
docker-compose exec django_app python manage.py generate_reviews --batch-size 2
```

### Running All Commands at Once
Make scripts executable and run them:
```bash
chmod +x scripts/startup.sh
./scripts/startup.sh

chmod +x scripts/run_all.sh
./scripts/run_all.sh
```

### Verify Services
Check the status of running containers:
```bash
docker-compose ps
```

## Monitoring and Maintenance

### View Logs
- **Ollama logs:**
  ```bash
  docker-compose logs ollama
  ```
- **Django app logs:**
  ```bash
  docker-compose logs django_app
  ```

### Database Management
- Create a superuser:
  ```bash
  docker-compose exec django_app python manage.py createsuperuser
  ```
- Access the Django admin interface at [http://localhost:8000/admin](http://localhost:8000/admin).

## Troubleshooting

### Common Issues

#### Ollama Service Not Starting
- Ensure ports are not in use.
- Check system resources.
- Review Ollama logs:
  ```bash
  docker-compose logs --tail=100 ollama
  ```

#### Database Connection Issues
- Verify PostgreSQL is running.
- Check database credentials in `.env`.
- Ensure the database exists and is accessible.

#### Timeout Errors
- Increase timeout value in the `OllamaService` class.
- Reduce batch size.
- Check system resources.

### Error Logs
- **Ollama logs:**
  ```bash
  docker-compose logs --tail=100 ollama
  ```
- **Django app logs:**
  ```bash
  docker-compose logs --tail=100 django_app
  ```

## Testing
Run tests using `pytest`:

### Run All Tests
```bash
pytest -v
```

### Run Specific Tests
- Test the Gemini service:
  ```bash
  pytest llmApp/tests/test_gemini_service.py -v
  ```
- Test custom commands:
  ```bash
  pytest llmApp/tests/test_commands.py -v
  ```

### View Test Coverage
Generate and open the HTML coverage report:
```bash
open htmlcov/index.html
```

---

Follow this guide to set up, run, and maintain the Hotel Content Generator with Ollama. For further assistance, refer to the documentation or contact the development team.
