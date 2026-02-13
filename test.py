import unittest
import main


class TestMainFunctions(unittest.TestCase):

    def test_process_expenses(self):
        prices = [47.50, 189.99, 320.40]
        result = main.process_expenses(prices)
        self.assertEqual(result, [54.625, 218.4885, 368.46])

    def test_sanitize_usernames(self):
        usernames = ["  DeltaForce  ", " Echo_Leader ", "  FoXTRot99"]
        result = main.sanitize_usernames(usernames)
        self.assertEqual(result, ["deltaforce", "echo_leader", "foxtrot99"])

    def test_identify_outliers(self):
        numbers = [12, 455, 87, 1024, 76, 305]
        result = main.identify_outliers(numbers)
        self.assertEqual(result, [455, 1024, 305])


if __name__ == "__main__":
    unittest.main()
