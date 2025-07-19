# Travel Packages API

A Flask application that retrieves travel package data from Google Cloud Storage.

## Setup

1. Install dependencies:
```bash
pip install -r flask_app/requirements.txt
```

2. Set up Google Cloud credentials:
   - Create a service account in Google Cloud Console
   - Download the service account key
   - Place the key file in the `flask_app` directory as `service-account-key.json`
   - Ensure the service account has access to the Cloud Storage bucket

3. Environment Variables:
   - Create a `.env` file in the `flask_app` directory
   - Add: `GOOGLE_APPLICATION_CREDENTIALS=./service-account-key.json`

## Running with Docker

1. Build the image:
```bash
cd flask_app
docker build -t travel-api .
```

2. Run the container:
```bash
docker run -p 5000:5000 travel-api
```

## API Endpoints

- `GET /`: Welcome message and API information
- `GET /packages`: Get all travel packages
- `GET /packages/search`: Search packages with filters
  - Query Parameters:
    - `flight_number`: Exact match
    - `departure_airport`, `arrival_airport`: Partial match
    - `room_type`: Exact match (Single, Double, Suite)
    - `min_price`, `max_price`: Price range
    - `min_departure_date`, `max_departure_date`: Date range (M/D/YYYY)
    - `min_arrival_date`, `max_arrival_date`: Date range (M/D/YYYY)
    - `min_check_in_date`, `max_check_in_date`: Date range (M/D/YYYY)
    - `min_check_out_date`, `max_check_out_date`: Date range (M/D/YYYY)

## Security Notes

- Never commit the `service-account-key.json` file to version control
- Keep your Google Cloud credentials secure and share them through secure channels
- The `.env` file is also excluded from version control for security
