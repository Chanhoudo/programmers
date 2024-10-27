import pyodbc

# 데이터베이스 연결 정보 설정
server = 'sentimentscout-review.database.windows.net'
database = 'ReviewDB'
username = 'testdb'
password = 'Tiger123'
driver = '{ODBC Driver 17 for SQL Server}'

# 데이터베이스에 연결
try:
    cnxn = pyodbc.connect(
        f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
    )
    cursor = cnxn.cursor()

    # StoreInfo 테이블에 있는 데이터 조회
    cursor.execute("SELECT * FROM StoreInfo")
    rows = cursor.fetchall()

    if rows:
        print("데이터베이스에 저장된 데이터:")
        for row in rows:
            print(row)
    else:
        print("데이터베이스에 저장된 데이터가 없습니다.")

    # 커서와 연결 종료
    cursor.close()
    cnxn.close()
except pyodbc.Error as e:
    print(f"Database error: {e}")
