import numpy as np
import pytest

import pydiver

def test_counts_from_sample():
    assert np.array_equal(pydiver.counts_from_sample(['a', 'a', 'b']), [2, 1])
