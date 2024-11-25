import pandas as pd
from sqlalchemy import create_engine

# TODO: This is a TODO
# NOTE: This is a note Comment
# HACK: this is not quite correct
# PERF: full optimized
# TODO: This is another todo item
# WARNING: this is a warning
# FIX: Fix me


def read_from_db(uri: str, comment: str) -> pd.DataFrame:
    engine = create_engine(uri, echo=False)
    conn = engine.connect()
    query = f"Call Export_to_Yahoo ('{comment}');"
    df = pd.read_sql(query, conn)
    return df


def export_as_csv(df: pd.DataFrame, filename: str) -> None:
    df.to_csv(filename, index=False)


def main():
    print("Export finance DB to yahoo via csv")
    url = "mysql+pymysql://jacques:1Kermit1@192.168.1.20/finance?charset=utf8mb4"
    tickers = read_from_db(url, "Export from local DB")
    export_as_csv(tickers, "yahoo.csv")
    print("Done")


if __name__ == "__main__":
    main()
