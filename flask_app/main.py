
from flask import Flask, jsonify, request
from google.cloud import storage
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Google Cloud Storage client
storage_client = storage.Client()
bucket_name = "travel_products"
file_name = "hotel_and_flight_packages.json"

def get_json_from_gcs():
    """Retrieve JSON data from Google Cloud Storage"""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    content = blob.download_as_text()
    return json.loads(content)

def parse_date(date_str):
    """Parse date string in M/D/YYYY format"""
    try:
        return datetime.strptime(date_str, "%m/%d/%Y")
    except:
        return None

def filter_packages(packages, params):
    """Filter packages based on search parameters"""
    filtered = packages

    # Text-based exact matches
    if params.get('flight_number'):
        filtered = [p for p in filtered if p['flight_number'].lower() == params['flight_number'].lower()]
    
    # Text-based partial matches
    for field in ['departure_airport', 'arrival_airport']:
        if params.get(field):
            search_term = params[field].lower()
            filtered = [p for p in filtered if search_term in p[field].lower()]
    
    # Room type exact match
    if params.get('room_type'):
        filtered = [p for p in filtered if p['room_type'].lower() == params['room_type'].lower()]
    
    # Price range
    if params.get('min_price'):
        filtered = [p for p in filtered if p['price'] >= float(params['min_price'])]
    if params.get('max_price'):
        filtered = [p for p in filtered if p['price'] <= float(params['max_price'])]
    
    # Date ranges
    for date_field in ['departure_date', 'arrival_date', 'check_in_date', 'check_out_date']:
        if params.get(f'min_{date_field}'):
            min_date = parse_date(params[f'min_{date_field}'])
            if min_date:
                filtered = [p for p in filtered if parse_date(p[date_field]) >= min_date]
        if params.get(f'max_{date_field}'):
            max_date = parse_date(params[f'max_{date_field}'])
            if max_date:
                filtered = [p for p in filtered if parse_date(p[date_field]) <= max_date]
    
    return filtered

@app.route("/")
def index():
    return """Travel Packages API
    Available endpoints:
    - /packages: Get all packages
    - /packages/search: Search packages with query parameters
        - flight_number: Exact match
        - departure_airport, arrival_airport: Partial match
        - room_type: Exact match (Single, Double, Suite)
        - min_price, max_price: Price range
        - min_departure_date, max_departure_date: Date range (M/D/YYYY)
        - min_arrival_date, max_arrival_date: Date range (M/D/YYYY)
        - min_check_in_date, max_check_in_date: Date range (M/D/YYYY)
        - min_check_out_date, max_check_out_date: Date range (M/D/YYYY)
    """

@app.route("/packages")
def get_packages():
    """Get all packages from the JSON file in GCS"""
    try:
        packages = get_json_from_gcs()
        return jsonify(packages)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/packages/search")
def search_packages():
    """Search packages with filters"""
    try:
        packages = get_json_from_gcs()
        filtered_packages = filter_packages(packages, request.args)
        return jsonify(filtered_packages)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int("5000"), debug=True)
