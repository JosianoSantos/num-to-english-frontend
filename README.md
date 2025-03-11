# Number to English API

This is a Django REST API that converts numbers into English words.

## Installation

### Running Manually


### Backend:

1. Create a virtual environment and install dependencies:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python manage.py runserver
   ```
### Frontend:

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```

### Running with Docker

1. Build and start the container:
   ```bash
   docker-compose up --build
   ```
2. The API will be available at `http://localhost:8000` and the frontend at `http://localhost:8080`.

### API Endpoints

- **GET /converter/num_to_english?number=12345**
  ```json
  { "number": 12345 }
  ```
- API Documentation:
  - Swagger: `/`