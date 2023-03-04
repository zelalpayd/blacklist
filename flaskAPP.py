from flask import Flask, request, jsonify
import json
from functions import checking

app = Flask(__name__)

# Define route for handling input data
@app.route('/<string:species>/<string:chr>:<int:start>_<int:stop>', methods=["GET"])
def check_coordinates(species,chr, start, stop):
    # Get species and coordinates from POST request data
    checking_status = checking(species, chr, start, stop)
    return checking_status

if __name__ == '__main__':
    app.run(debug=True)
