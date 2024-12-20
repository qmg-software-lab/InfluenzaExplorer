import logging
import sqlite3
import pandas as pd


# init terminology
def terminology_add_a_value_set():

    qry_add_value_set = """
        -- add a value set to your terminology db
        WITH value_set_code AS (
            SELECT *
            FROM Shared.terminology.ValueSetCode
            )
        SELECT DISTINCT
              vsd.ValueSetNM
            , vsd.ValueSetReferenceID
            , vsc.CodeSystemNM
            , vsd.AuthorityDSC
        FROM Shared.terminology.ValueSetCode vsc
        JOIN Shared.terminology.ValueSetDescription AS vsd ON vsc.ValueSetGUID = vsd.ValueSetGUID
        WHERE  vsc.CodeSystemNM LIKE '%cpt%'
        --AND vsc.CodeCD IN (
        --AND vsc.CodeCD = 
        ORDER BY vsd.ValueSetNM 
    """
    try:
        # odbc tunnel
        cnx = sqlite3.connect('terminology.db')
        result_df = pd.read_sql(qry_add_value_set, cnx)
    except Exception as e_terminology_add_a_value_set_cnx:
        logging.error(e_terminology_add_a_value_set_cnx)
    finally:


        return result_df

if __name__ == "__main__":
    print(terminology_add_a_value_set())