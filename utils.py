import pytz
from datetime import datetime
import uuid

def ist_to_timezone(cls, target_tz):
    ist = pytz.timezone("Asia/Kolkata")
    target = pytz.timezone(target_tz)
    localized = ist.localize(cls["datetime"])
    converted_time = localized.astimezone(target)
    return {
        "id": cls["id"],
        "name": cls["name"],
        "datetime": converted_time.isoformat(),
        "instructor": cls["instructor"],
        "available_slots": cls["available_slots"]
    }

def generate_id():
    return str(uuid.uuid4())

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
