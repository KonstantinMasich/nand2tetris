from test_utils.commons import run_tests_with_tool


def test_proj_01():
    """Tests for Project 01."""
    run_tests_with_tool(tool='HardwareSimulator', target_dir='p01')
