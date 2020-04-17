import sqlit3
db_file = 'curing'

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    print('stage a\n')
    return conn

''' GET DAILY AVERAGES AND DROP TABLE '''
if __name__ == '__main__':
    cur = create_connection(db_file)
    cur.execute('''SELECT * FROM readings ''')
