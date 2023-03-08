import unittest

from prsmsp.models.response import Response


class TestRespnoseModel(unittest.TestCase):

    def test_equality(self):
        r1 = Response(200, 21, 'real response')
        r2 = Response(200, 21, 'real response')
        r3 = Response(400, 21, 'real response')
        self.assertEqual(r1, r2)
        self.assertNotEqual(r1, r3)


if __name__ == "__main__":
    unittest.main()
