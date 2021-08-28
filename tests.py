"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn(b"having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get('/')
        self.assertIn(b'Please RSVP', result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        # FIXME: check that once we log in we see party details--but not the form!

        # Test you don't see RSVP form
        result = self.client.get('/')
        self.assertNotIn(b'Please RSVP', result.data)

        # Test you see the party details
        result = self.client.get('/')
        self.assertIn(b'Party Details', result.data)


    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        # FIXME: write a test that mel can't invite himself

        rsvp_info = {'name': "Mel Melitpolski", 'email': "mel@ubermelon.com"}
        result = self.client.post("/rsvp", data=rsvp_info, follow_redirects=True)

        result = self.client.get('/')
        self.assertTrue(b'Sorry, Mel. This is kind of awkward.', result.data)


if __name__ == "__main__":
    unittest.main()
