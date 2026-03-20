from src.fetch_timecard import fetch_and_save
from src.analyze import analyze_timecard


def main():
    date_from = "2020-01-01"
    date_to = "2020-12-31"

    df = fetch_and_save(date_from, date_to)

    summary = analyze_timecard(df)

    print(summary)


if __name__ == "__main__":
    main()