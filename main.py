import raspi
from flask import *

app = Flask(__name__)
raspi = raspi.Raspi()

# Index route
@app.route("/")
def index():
  # Read the value of the sensor
  value = raspi.read_sensor()
  # Render the index.html template passing the value of the sensor
  return render_template('index.html', sensor_value=value)

# About route
@app.route("/about")
def about():
  # Render the about.html template
  return render_template('about.html')

# Change LED value POST request.
@app.route("/change_led_status/<int:status>", methods=['POST'])
def change_led_status(status):
  # Check the value of the parameter
  if status == 0:
    raspi.change_led(False)
  elif status == 1:
    raspi.change_led(True)
  else:
    return ('Error', 500)
  return ('', 200)

# Starts the app listening to port 5000 with debug mode
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
