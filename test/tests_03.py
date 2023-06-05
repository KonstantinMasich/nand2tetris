from test_utils.commons import run_tests_with_tool


def test_proj_03():
    """Tests for Project 03."""
    run_tests_with_tool(tool='HardwareSimulator', target_dir='p03/a')
    run_tests_with_tool(tool='HardwareSimulator', target_dir='p03/b')
