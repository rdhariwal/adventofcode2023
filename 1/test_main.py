from main import compute, enhanced_compute

def sum():
    return 2

def test_compute():
    assert compute("input") == 54630

def test_compute_test_input():
    assert compute("input_test") == 171

def test_enhanced_compute():
    assert enhanced_compute("input_test_2") == 281