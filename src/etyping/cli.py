from __future__ import annotations

import argparse
import getpass
import logging
import sys
import typing

import etyping
import etyping.game
import etyping.webdriver

_LOGGING_FORMAT = "%(asctime)s %(levelname)s %(pathname)s %(message)s"
logging.basicConfig(
    format=_LOGGING_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S%z",
    handlers=[logging.StreamHandler()],
    level=logging.INFO,
)


def _run(
    email: typing.Optional[str] = None,
    password: typing.Optional[str] = None,
    headless: bool = False,
    game_type: str = "roma",
) -> None:
    if email is None or password is None:
        credentials = _input_login_credentials()
    else:
        credentials = etyping.game._LoginCredentials(email, password)
    with etyping.webdriver.create_firefox_driver(headless=headless) as driver:
        etyping.game.run(
            driver=driver,
            credentials=credentials,
            game_type=etyping.game._type_from_str(game_type),
        )


def _input_login_credentials() -> etyping.game._LoginCredentials:
    return etyping.game._LoginCredentials(
        email=input("Email: "),
        password=getpass.getpass("Password: "),
    )


def _add_run_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--headless",
        action="store_true",
        default=False,
        required=False,
        help="run in headless mode",
    )
    parser.add_argument(
        "--email",
        type=str,
        required=False,
        default=None,
        help="login email",
    )
    parser.add_argument(
        "--password",
        type=str,
        required=False,
        default=None,
        help="login password",
    )
    parser.add_argument(
        "--game-type",
        type=str,
        required=False,
        default="roma",
        choices=["roma", "en"],
    )


def main(argv: typing.Sequence[str] | None = None) -> None:
    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(prog="etyping")

    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {etyping.__version__}",
    )

    subpersers = parser.add_subparsers(dest="subcommand")
    sub_run = subpersers.add_parser("run", help="play etyping.")
    _add_run_options(sub_run)

    args = parser.parse_args(argv)

    if args.subcommand == "run":
        _run(
            headless=args.headless,
            email=args.email,
            password=args.password,
            game_type=args.game_type,
        )
    else:
        parser.print_help()

    args = parser.parse_args(argv)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
