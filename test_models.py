import unittest
from models import Band, Venue, Concert, Session

class TestConcertModels(unittest.TestCase):
    def setUp(self):
        self.session = Session()

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_band(self):
        band = Band(name='Sauti Sol', hometown='Nairobi')
        self.session.add(band)
        self.session.commit()
        self.assertEqual(band.name, 'Sauti Sol')

    def test_create_venue(self):
        venue = Venue(title='Kasarani Stadium', city='Nairobi')
        self.session.add(venue)
        self.session.commit()
        self.assertEqual(venue.title, 'Kasarani Stadium')

    def test_create_concert(self):
        band = Band(name='Sauti Sol', hometown='Nairobi')
        venue = Venue(title='Kasarani Stadium', city='Nairobi')
        concert = Concert(date='2023-12-01', band=band, venue=venue)

        self.session.add(band)
        self.session.add(venue)
        self.session.add(concert)
        self.session.commit()

        self.assertEqual(concert.band.name, 'Sauti Sol')
        self.assertEqual(concert.venue.title, 'Kasarani Stadium')

if __name__ == '__main__':
    unittest.main()
