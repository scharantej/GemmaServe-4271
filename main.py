
from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# Sample data objects
devices = [
    {"serial_number": "1234567890", "name": "Device 1", "status": "Online"},
    {"serial_number": "0987654321", "name": "Device 2", "status": "Offline"},
]

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/devices")
def devices():
    return render_template("devices.html", devices=devices)

@app.route("/device/<serial_number>")
def device(serial_number):
    device = next((device for device in devices if device["serial_number"] == serial_number), None)
    if device:
        return render_template("device.html", device=device)
    else:
        return "Device not found", 404

@app.route("/control/<serial_number>/<command>")
def control(serial_number, command):
    device = next((device for device in devices if device["serial_number"] == serial_number), None)
    if device:
        # Here, you would typically send the command to the Gemma C++ device.
        # For the purpose of this example, we simply update the device status.
        device["status"] = "On" if command == "on" else "Off"
        return jsonify({"status": "OK"})
    else:
        return "Device not found", 404

@app.route("/status/<serial_number>")
def status(serial_number):
    device = next((device for device in devices if device["serial_number"] == serial_number), None)
    if device:
        return jsonify(device)
    else:
        return "Device not found", 404

if __name__ == "__main__":
    app.run(debug=True)
