from qgame import quotegame
from qgame_scraper import quotes_scraper


def is_accessible(path, mode="r"):
    """Checks existence of csv file with quotes

    Parameters
    ----------
    path : str
        path to csv file

    mode : str, optional
        opens write mode, by default "r"

    Returns
    -------
    bool
        true or false
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


def main():
    if (is_accessible("quote_db.csv", "r")):
        quotegame()

    else:
        quotes_scraper()
        main()


if __name__ == "__main__":
    main()
