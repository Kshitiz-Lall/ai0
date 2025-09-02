# FastAPI + Uvicorn Web Scraper App

A FastAPI application with web scraping capabilities using BeautifulSoup and environment variable configuration.

## Features
- Basic FastAPI endpoints
- Web scraping functionality with BeautifulSoup
- Environment variable configuration with python-dotenv
- Dependency management with pyproject.toml

## Setup

### 1. Install dependencies
```
pip install -r requirements.txt
```

Or using the pyproject.toml:
```
pip install -e .
```

### 2. Environment Configuration
Copy the example environment file and configure your settings:
```
copy .env.example .env
```

Edit `.env` with your preferred settings:
- `DEBUG`: Enable/disable debug mode
- `USER_AGENT`: Custom user agent for web scraping
- `OPENAI_API_KEY`: Your OpenAI API key (if using AI features)
- `SYSTEM_PROMPT`: Custom system prompt for AI analysis

## Run the server
```
uvicorn app:app --reload
```

## API Endpoints

- `GET /` - Hello World endpoint with environment info
- `GET /scrape/{url}` - Scrape a website and return content analysis
- `GET /config` - View current configuration (debug purposes)

### Examples
- http://127.0.0.1:8000
- http://127.0.0.1:8000/scrape/example.com
- http://127.0.0.1:8000/scrape/https://python.org
- http://127.0.0.1:8000/config

Visit http://127.0.0.1:8000/docs for interactive API documentation.

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `false` |
| `USER_AGENT` | User agent for web requests | Chrome default |
| `API_KEY` | General API key | `""` |
| `OPENAI_API_KEY` | OpenAI API key | `""` |
| `SYSTEM_PROMPT` | AI system prompt | Default analysis prompt |
| `HOST` | Server host | `127.0.0.1` |
| `PORT` | Server port | `8000` |
