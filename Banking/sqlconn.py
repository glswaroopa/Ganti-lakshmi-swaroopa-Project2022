class sqlconn:
    import pyodbc

    """description of class"""

    def sqllogin(query):
        conn_str = ("Driver={SQL Server};"
            "Server=INCDE01D011G01;"
            "Database=Banking;"
            "UID=banking;"
            "PWD=User@123;")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        return conn








