from m_12_2 import Runner
import unittest


class TestRunner(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        a = Runner('name')
        for i in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        a = Runner('name_2')
        for i in range(10):
            a.run()
        self.assertEqual(a.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        a = Runner('name')
        b = Runner('name_2')
        for i in range(10):
            a.walk()
        for i in range(10):
            b.run()
        self.assertNotEqual(a.distance, b.distance)


if __name__ == '__main__':
    unittest.main()
