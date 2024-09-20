from flask import Flask, jsonify, request
from models import Session, Band, Venue, Concert

app = Flask(__name__)
session = Session()

@app.route('/bands', methods=['GET'])
def get_bands():
    bands = session.query(Band).all()
    return jsonify([{'name': band.name, 'hometown': band.hometown} for band in bands])

@app.route('/venues', methods=['GET'])
def get_venues():
    venues = session.query(Venue).all()
    return jsonify([{'title': venue.title, 'city': venue.city} for venue in venues])

@app.route('/concerts', methods=['GET'])
def get_concerts():
    concerts = session.query(Concert).all()
    return jsonify([{'date': concert.date, 'band': concert.band.name, 'venue': concert.venue.title} for concert in concerts])

if __name__ == '__main__':
    app.run(debug=True)
