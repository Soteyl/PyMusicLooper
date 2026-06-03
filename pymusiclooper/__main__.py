import os

# Set stable numba JIT cache dir before numba (or anything that imports numba) is touched.
# In onefile PyInstaller mode the default cache path is inside the temp-extracted bundle,
# which is recreated on every run, destroying the compiled cache each time.
os.environ.setdefault(
    "NUMBA_CACHE_DIR",
    os.path.join(os.path.expanduser("~"), ".cache", "pymusiclooper", "numba"),
)

import logging

from pymusiclooper.cli import cli_main


def cli():
    try:
        cli_main(prog_name="pymusiclooper")
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    cli()
