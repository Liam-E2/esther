import sys
from src.utils import get_project_root, configure_logs
from src.db.create_db import create_database


def main(argv: list) -> int:
    """
    Parses cmdline args to run esther.
    Returns int.
    """
    logger = configure_logs("mainlog", 'main', 'main.txt')
    logger.debug("Starting esther")

    create_database('esther.db')


if __name__ == '__main__':
    main(sys.argv)

