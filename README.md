# Receipt Processor API

This is a Python FastAPI-based receipt processing service. The API allows users to submit receipts for processing and retrieve points based on specific rules.

## Features
- Submit a receipt for processing.
- Retrieve points awarded for a processed receipt.
- Built using **FastAPI** for high performance.
- Containerized using **Docker**.

## Getting Started
### 1. Clone the Repository
```bash
git clone https://github.com/ytc338/receipt-processor.git
cd receipt-processor
```

### 2. Build and Run with Docker
```bash
docker compose up --build
```
This command will:
- Build the Docker image
- Start the FastAPI server in a container

### 3. API Endpoints
| Method | Endpoint                  | Description                         |
|--------|---------------------------|-------------------------------------|
| POST   | `/receipts/process`       | Submits a receipt for processing   |
| GET    | `/receipts/{id}/points`   | Retrieves awarded points           |

### 4. Testing the API
To test via `cURL`:
```bash
curl -X POST "http://localhost:8000/receipts/process" \
     -H "Content-Type: application/json" \
     -d '{"retailer": "M&M Corner Market", "purchaseDate": "2024-02-05", "purchaseTime": "13:01", "items": [{"shortDescription": "Mountain Dew 12PK", "price": "6.49"}], "total": "6.49"}'
```

### 5. Stopping the Service
To stop the Docker container:
```bash
docker compose down
```

## Project Structure
```
receipt-processor/
│── app/
│   ├── logic/  # Business logic module
│   ├── models.py  # Pydantic models
│   ├── server.py  # FastAPI server
│── Dockerfile
│── docker-compose.yml
│── requirements.txt
│── README.md
```
