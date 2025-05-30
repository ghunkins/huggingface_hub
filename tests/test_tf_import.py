import sys
import unittest

from old_huggingface_hub.utils import is_tf_available


def require_tf(test_case):
    """
    Decorator marking a test that requires TensorFlow.

    These tests are skipped when TensorFlow is not installed.

    """
    if not is_tf_available():
        return unittest.skip("test requires Tensorflow")(test_case)
    else:
        return test_case


@require_tf
def test_import_old_huggingface_hub_does_not_import_tensorflow():
    # `import old_huggingface_hub` is not necessary since old_huggingface_hub is already imported at the top of this file,
    # but let's keep it here anyway just in case
    import old_huggingface_hub  # noqa

    assert "tensorflow" not in sys.modules
