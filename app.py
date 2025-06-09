from flask import Flask, render_template, request, jsonify, redirect, url_for


from utils import ist_to_timezone, generate_id,save_data


import pytz,json
import logging

app = Flask(__name__, static_folder='static', template_folder='templates')

logging.basicConfig(level=logging.INFO)
CLASSES_FILE = 'data/classes.json'
BOOKINGS_FILE = 'data/bookings.json'

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/bookings-page")
def bookings_page():
    return render_template("bookings.html")



def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)




@app.route('/book', methods=['POST'])
def book_class():
    class_id = request.form.get('class_id')
    client_name = request.form.get('client_name')
    client_email = request.form.get('client_email')

    if not class_id or not client_name or not client_email:
        return "All fields are required", 400

    classes = load_data(CLASSES_FILE)
    class_found = None

    for c in classes:
        if c['id'] == class_id:
            class_found = c
            break

    if not class_found:
        return "Class not found", 404

    if class_found['available_slots'] <= 0:
        return "No available slots", 400

    # Decrease slot count
    class_found['available_slots'] -= 1
    save_data(CLASSES_FILE, classes)

    bookings = load_data(BOOKINGS_FILE)
    booking = {
        "booking_id": generate_id(),
        "class_id": class_found['id'],
        "class_name": class_found['name'],
        "datetime": class_found['datetime'],
        "instructor": class_found['instructor'],
        "client_name": client_name,
        "client_email": client_email
    }
    bookings.append(booking)
    save_data(BOOKINGS_FILE, bookings)

    return redirect(url_for('index'))

@app.route("/api/classes", methods=["GET"])
def get_classes():
    classes = load_data(CLASSES_FILE)

    return jsonify(classes)

@app.route("/bookings")
def get_bookings():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Missing email"}), 400

    bookings = load_data(BOOKINGS_FILE)
    classes = {cls["id"]: cls for cls in load_data(CLASSES_FILE)}

    filtered = []
    for booking in bookings:
        if booking["client_email"] == email:
            cls = classes.get(booking["class_id"])
            if cls:
                filtered.append({
                    "class_name": cls["name"],
                    "instructor": cls["instructor"],
                    "datetime": cls["datetime"],
                    "client_name": booking["client_name"]
                })

    return jsonify(filtered)



if __name__ == "__main__":
    app.run(debug=True)
