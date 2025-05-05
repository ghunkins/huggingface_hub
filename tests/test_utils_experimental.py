import unittest
import warnings
from unittest.mock import patch

from old_huggingface_hub.utils import experimental


@experimental
def dummy_function():
    return "success"


class TestExperimentalFlag(unittest.TestCase):
    def test_experimental_warning(self):
        with patch("old_huggingface_hub.constants.HF_HUB_DISABLE_EXPERIMENTAL_WARNING", False):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                self.assertEqual(dummy_function(), "success")
            self.assertEqual(len(w), 1)

    def test_experimental_no_warning(self):
        with patch("old_huggingface_hub.constants.HF_HUB_DISABLE_EXPERIMENTAL_WARNING", True):
            with warnings.catch_warnings(record=True) as w:
                warnings.simplefilter("always")
                self.assertEqual(dummy_function(), "success")
            self.assertEqual(len(w), 0)
