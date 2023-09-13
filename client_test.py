import unittest
from client3 import getDataPoint
from client3 import getRatio # Imported to test

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion added ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Assertion added ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Additional unit tests for getRatio ------------ """
  def test_getRatio_calculatePriceAGreaterThanPriceB(self):
    pairs = [
      {'price_a': 1236.59, 'price_b': 746.3},
      {'price_a': 758, 'price_b': 248.7},
      {'price_a': 857, 'price_b': 648}
    ]

    for pair in pairs:
      self.assertEqual(getRatio(pair['price_a'], pair['price_b']), (pair['price_a'] / pair['price_b']))

  def test_getRatio_calculatePriceALessThanPriceB(self):
    pairs = [
      {'price_a': 758.75, 'price_b': 1267.3},
      {'price_a': 486, 'price_b': 958.23},
      {'price_a': 45, 'price_b': 316}
    ]

    for pair in pairs:
      self.assertEqual(getRatio(pair['price_a'], pair['price_b']), (pair['price_a'] / pair['price_b']))

  def test_getRatio_zeroDivisionError(self):
    pairs = [
      {'price_a': 758.75, 'price_b': 0},
      {'price_a': 486, 'price_b': 0},
    ]

    for pair in pairs:
      self.assertEqual(getRatio(pair['price_a'], pair['price_b']), None)

if __name__ == '__main__':
    unittest.main()
