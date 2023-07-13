import json


def test_fails_with_no_args(script_runner):
    result = script_runner.run(['run.py'])
    assert result.returncode == 2


def test_f_required(script_runner):
    result = script_runner.run(['run.py', '-f spend,clicks'])
    assert result.returncode == 0
    # assert result.stdout == '3.2.1\n'
    # assert result.stderr == ''


def test_f_wrong_field(script_runner):
    result = script_runner.run(['run.py', '-f id,clicks'])
    assert result.returncode == 1
    # assert result.stdout == '3.2.1\n'
    # assert result.stderr == ''


def is_valid_json(json_string):
    try:
        json.loads(json_string)
        return True
    except json.JSONDecodeError:
        return False


def test_result_is_valid_json(script_runner):
    result = script_runner.run(['run.py', '-f spend,clicks'])
    assert is_valid_json(result.stdout)
