from django.test import SimpleTestCase
import json
from core.forms import PrettyJSONEncoder


class PrettyJSONEncoderTests(SimpleTestCase):
    def test_pretty_json_encoder_initialization(self):
        """Test that PrettyJSONEncoder initializes with custom arguments."""
        encoder = PrettyJSONEncoder(indent=4, sort_keys=True)
        self.assertEqual(encoder.indent, 2)
        self.assertTrue(encoder.sort_keys)

    def test_pretty_json_encoder_serialization(self):
        """Test that PrettyJSONEncoder serializes JSON objects with proper formatting."""
        data = {"b": 2, "a": 1}
        expected_json = '{\n  "a": 1,\n  "b": 2\n}'
        result = json.dumps(data, cls=PrettyJSONEncoder, indent=2, sort_keys=True)
        self.assertEqual(result, expected_json)

    def test_pretty_json_encoder_with_invalid_data(self):
        """Test that PrettyJSONEncoder raises an exception for unserializable objects."""

        class UnserializableObject:
            pass

        unserializable = UnserializableObject()

        with self.assertRaises(TypeError):
            json.dumps(unserializable, cls=PrettyJSONEncoder, indent=2, sort_keys=True)
