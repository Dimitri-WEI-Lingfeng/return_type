def test_mypy_plugin():
    from mypy import api

    result = api.run(
        [
            "--config-file",
            "./tests/mypy.ini",
            "./tests/mypy_test.py",
            "--show-traceback",
        ]
    )
    print(result)
    assert result[2] == 0
