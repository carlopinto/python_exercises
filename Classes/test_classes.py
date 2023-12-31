import unittest

import sms
from rectangle import Point, Rectangle
from cards import *

class TestClasses(unittest.TestCase):

    def test_add_message_to_inbox(self):
        my_inbox = sms.SMS_store()
        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")

        self.assertEqual(type(("0123","10:30","Hello, how are you?")), tuple)
        self.assertEqual(my_inbox.message_count(), 1)

    def test_inbox_count(self):
        """ """
        my_inbox = sms.SMS_store()
        my_inbox.clear()
        self.assertEqual(my_inbox.message_count(), 0)

        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")
        self.assertEqual(my_inbox.message_count(), 1)

        my_inbox.add_new_arrival("0123","10:32","I am fine!")
        my_inbox.add_new_arrival("0123","10:35","Bye")
        self.assertEqual(my_inbox.message_count(), 3)

    def test_create_inbox(self):
        """ """
        my_inbox = sms.SMS_store()
        my_inbox.clear()
        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")
        my_inbox.add_new_arrival("0123","10:32","I am fine!")
        my_inbox.add_new_arrival("0123","10:35","Bye")

        self.assertEqual(my_inbox.message_count(), 3)

    def test_get_unread(self):
        """ """
        my_inbox = sms.SMS_store()
        my_inbox.clear()
        self.assertEqual(my_inbox.get_unread_indexes(), [])
        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")
        my_inbox.add_new_arrival("0123","10:32","I am fine!")
        my_inbox.add_new_arrival("0123","10:35","Bye")

        self.assertEqual(my_inbox.get_unread_indexes(), [0,1,2])

    def test_get_message(self):
        """ """
        my_inbox = sms.SMS_store()
        my_inbox.clear()
        self.assertEqual(my_inbox.get_message(0), None)
        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")
        my_inbox.add_new_arrival("0123","10:32","I am fine!")
        my_inbox.add_new_arrival("0123","10:35","Bye")
        # print(type(my_inbox.get_message(0)))
        self.assertEqual(my_inbox.get_message(0), ("0123","10:30","Hello, how are you?"))

    def test_clear_inbox(self):
        """ """
        my_inbox = sms.SMS_store()
        my_inbox.clear()
        my_inbox.add_new_arrival("0123","10:30","Hello, how are you?")
        my_inbox.add_new_arrival("0123","10:32","I am fine!")
        my_inbox.add_new_arrival("0123","10:35","Bye")
        self.assertEqual(my_inbox.message_count(), 3)
        my_inbox.clear()
        self.assertEqual(my_inbox.message_count(), 0)


    def test_point_distance_from_origin(self):
        """"""
        p = Point(10,6)
        self.assertEqual(str(p), "(10, 6)")
        self.assertEqual(p.distance_from_origin(), 11.661903789690601)

    def test_point_halfway(self):
        """"""
        p = Point(10,6)
        p2 = Point(16,-2)
        self.assertEqual(str(p.halfway(p2)), "(13.0, 2.0)")

    def test_point_slope_from_origin(self):
        """"""
        p = Point(5, 10)
        self.assertEqual(p.slope_from_origin(), 2.0)
        p2 = Point(0, 10)
        self.assertEqual(p2.slope_from_origin(), None)

    def test_point_slope_from_target(self):
        """"""
        p = Point(5, 10)
        p2 = Point(0, 2)
        self.assertEqual(p.slope_from_target(p2), 1.6)

    def test_point_get_line_to(self):
        """"""
        p = Point(5, 10)
        p2 = Point(0, 2)
        self.assertEqual(p.get_line_to(p2), (1.6, 2.0))
        

    def test_rectangle(self):
        """"""
        r = Rectangle(Point(10,5), 100, 50)

        self.assertEqual(str(r), "((10, 5), 100, 50)")
        r.grow(25, -10)
        self.assertEqual(str(r), "((10, 5), 125, 40)")
        r.move(-10, 10)
        self.assertEqual(str(r), "((0, 15), 125, 40)")

    def test_area_per_rectangle(self):
        """"""
        r = Rectangle(Point(0, 0), 10, 5)
        self.assertEqual(r.area(), 50)
        self.assertEqual(r.perimeter(), 30)

    def test_flip_rectangle(self):
        """"""
        r = Rectangle(Point(100, 50), 10, 5)

        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        r.flip()
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)

    def test_rectangle_contains(self):
        """"""
        r = Rectangle(Point(0, 0), 10, 5)

        self.assertTrue(r.contains(Point(0, 0)))
        self.assertTrue(r.contains(Point(3, 3)))
        self.assertFalse(r.contains(Point(3, 7)))
        self.assertFalse(r.contains(Point(3, 5)))
        self.assertTrue(r.contains(Point(3, 4.99999)))
        self.assertFalse(r.contains(Point(-3, -3)))

    def test_rectangle_overlap(self):
        """"""
        r1 = Rectangle(Point(0, 0), 3, 3)
        r2 = Rectangle(Point(2, 2), 3, 3)

        self.assertTrue(r1.rectangles_overlap(r2))

class TestCards(unittest.TestCase):

    def test_cards_value_suit(self):
        """"""
        card1 = Card(1, 1)
        card2 = Card(2, 13)
        self.assertTrue(card1 < card2)

    def test_same_card(self):
        """"""
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        self.assertTrue(card1 == card2)

    def test_cards_value_rank(self):
        """"""
        card1 = Card(1, 3)
        card2 = Card(1, 5)
        self.assertTrue(card1 < card2)
        card2.rank = 11
        self.assertTrue(card1 < card2)

    def test_cards_value_rank_ace(self):
        """ Aces are ranked higher than Kings """
        card1 = Card(1, 1)
        card2 = Card(1, 5)
        self.assertTrue(card1 > card2)
        card2.rank = 13
        self.assertTrue(card1 > card2)

        card1.rank = 12
        card2.rank = 1
        self.assertTrue(card1 < card2)

    def test_card_from_str(self):
        """"""
        card = Card(1, 1)
        self.assertTrue(card.suit == 1)
        self.assertTrue(card.rank == 1)

        card = card.from_str("Queen of Hearts")
        self.assertTrue(card.suit == 2)
        self.assertTrue(card.rank == 12)

    def test_deck_hand(self):
        """"""
        deck = Deck()
        deck.shuffle()
        hand = Hand("player")
        deck.deal([hand], 5)
        self.assertTrue(len(hand.cards) == 5)

    def test_deck_remove(self):
        """"""
        deck = Deck()
        deck.shuffle()
        tot_num_cards = len(deck.cards)
        if deck.remove(Card(1, 2)):
            self.assertTrue(len(deck.cards) == tot_num_cards - 1)
            
        # That card has been removed already
        self.assertFalse(deck.remove(Card(1, 2)))
        # That card does not exist in the deck
        self.assertFalse(deck.remove(Card(5, 22)))

    def test_old_maid_remove(self):
        """"""
        game = CardGame()
        hand = OldMaidHand("carlo")
        game.deck.deal([hand], 13)
        count = len(hand.cards)

        hand.remove_matches()
        self.assertTrue(count >= len(hand.cards))

if __name__ == '__main__':
    unittest.main()