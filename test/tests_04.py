from test_utils.commons import run_tests_with_tool


def test_proj_04():
    """Tests for Project 04."""
    run_tests_with_tool(tool='CPUEmulator',
                        target_dir='p04/fill',
                        ignored=['p04/fill/Fill.tst'])
