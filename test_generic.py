"""Test cases"""
import json


def test_fails_with_no_args(script_runner):
    """Test fails when run with no arguments"""
    result = script_runner.run(['run.py'])
    assert result.returncode == 2


def test_f_required(script_runner):
    """Test runs successfully with required argument"""
    result = script_runner.run(['run.py', '-f spend,clicks'])
    assert result.returncode == 0


def test_f_wrong_field(script_runner):
    """Test failing with wrong field name"""
    result = script_runner.run(['run.py', '-f id,clicks'])
    assert result.returncode == 1


def is_valid_json(json_string):
    """Functions that checks if a string contains a valid JSON object"""
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


def test_result_is_valid_json(script_runner):
    """Test that output is valid JSON"""
    result = script_runner.run(['run.py', '-f spend,clicks'])
    assert is_valid_json(result.stdout)
