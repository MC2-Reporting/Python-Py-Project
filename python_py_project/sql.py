# inspire: https://github.com/MC2-Reporting/CPD/blob/master/TOOL/cpd/tools.py

from sqlalchemy.engine import URL, create_engine


def _get_connection(
    server: str = "MSTM1BDB33\\DB01", database: str = "REPORTING", **kwargs
) -> sqlalchemy.engine.Engine:
    """Create sql connection engine to SQL Server."""

    driver = "ODBC Driver 17 for SQL Server"
    con_string = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};Trusted_Connection=yes"
    con_url = URL.create("mssql+pyodbc", query={"odbc_connect": con_string})
    # connect to server db
    engine = create_engine(con_url, **kwargs)
    return engine
