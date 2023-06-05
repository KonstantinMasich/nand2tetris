from test_utils.commons import run_tests_with_tool


def test_proj_05():
    """Tests for Project 05."""
    run_tests_with_tool(tool='HardwareSimulator',
                        target_dir='p05',
                        ignored=['p05/Memory.tst'])
