from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import func


Base = declarative_base()

# Band model
class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)

    # Relationship with concerts
    concerts = relationship('Concert', back_populates='band')

    def __repr__(self):
        return f'<Band(name={self.name}, hometown={self.hometown})>'

    def venues(self):
        # Return a collection of venues where this band has performed
        return [concert.venue for concert in self.concerts]

    def play_in_venue(self, venue, date):
        # Create a new concert for this band in the given venue on the given date
        concert = Concert(band=self, venue=venue, date=date)
        return concert

    def all_introductions(self):
        # Return an array of all introductions for this band
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]

    @classmethod
    def most_performances(cls, session):
        # Return the band with the most concerts
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count(Concert.id).desc()).first()

# Venue model
class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)

    # Relationship with concerts
    concerts = relationship('Concert', back_populates='venue')

    def __repr__(self):
        return f'<Venue(title={self.title}, city={self.city})>'

    def bands(self):
        # Return a collection of bands that have performed at this venue
        return [concert.band for concert in self.concerts]

    def concert_on(self, date):
        # Find and return the concert on the given date
        return next((concert for concert in self.concerts if concert.date == date), None)

    def most_frequent_band(self):
        # Return the band with the most concerts at this venue
        band_count = {}
        for concert in self.concerts:
            band = concert.band
            band_count[band] = band_count.get(band, 0) + 1
        return max(band_count, key=band_count.get)

# Concert model
class Concert(Base):
    __tablename__ = 'concerts'

    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    date = Column(String)

    # Relationships
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def __repr__(self):
        return f'<Concert(band={self.band.name}, venue={self.venue.title}, date={self.date})>'

    def hometown_show(self):
        # Return True if the concert is in the band's hometown
        return self.venue.city == self.band.hometown

    def introduction(self):
        # Return the band's introduction for this concert
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

# Database setup
engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)
