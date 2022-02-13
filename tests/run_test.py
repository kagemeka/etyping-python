import unittest

import pytest

import etyping.cli
import etyping.game
import etyping.webdriver


class Test(unittest.TestCase):
    @pytest.mark.skip(reason="credentials input is needed")
    def test_run(self) -> None:
        etyping.cli._run(headless=True)


if __name__ == "__main__":
    unittest.main()
