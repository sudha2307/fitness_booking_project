# Fitness Booking API

A simple backend API for booking fitness classes like Yoga, Zumba, and HIIT.  
Built with Python and Flask, using JSON files for data storage.

---

## Features

- List available fitness classes with details (name, date/time, instructor, available slots).  
- Book a class if slots are available.  
- View all bookings by client email.  
- Basic input validation and error handling.  

---

## Setup Instructions

### Prerequisites

- Python 3.7+ installed  
- `pip` package manager  

### Installation

1. Clone this repository:  
   ```bash
   git clone https://github.com/sudha2307/fitness_booking_project.git
   cd fitness_booking_project

2. Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the app:
python app.py

### Sample cURL Requests
## Get classes:

  - curl http://localhost:5000/api/classes
   
## Book a class:

   - curl -X POST http://localhost:5000/book -H "Content-Type: application/json" \
   -d '{"class_id": "class1", "client_name": "ABC", "client_email": "ABc@example.com"}'

## Get bookings for email:
   - curl "http://localhost:5000/bookings?email=john@example.com"

