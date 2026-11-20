import unittest
from main import expand

class Tests(unittest.TestCase):
    def test_simple_encoding(self):
        self.assertEqual(expand("/users/{name}", {"name":"Ada Lovelace"}), "/users/Ada%20Lovelace")
    def test_reserved_expansion(self):
        self.assertEqual(expand("{+path}", {"path":"/docs/a?b=c"}), "/docs/a?b=c")
    def test_query_expansion(self):
        self.assertEqual(expand("/search{?q,page}", {"q":"hello world","page":2}), "/search?q=hello%20world&page=2")
    def test_missing_query_variables(self):
        self.assertEqual(expand("/search{?q}", {}), "/search")
    def test_rejects_objects(self):
        with self.assertRaises(ValueError):
            expand("/{value}", {"value":{"nested":1}})

if __name__ == "__main__":
    unittest.main()
