import dataset
dialect = 'postgresql'
driver = 'pg8000'
username = 'sysadmin'
password = 'flipper'
host = 'localhost'
port = '5432'
database = 'kenamju'
baseStr = "{}+{}://{}:{}@{}:{}/{}"
engineStr = baseStr.format(dialect, driver, username, password, host, port, database)

db = dataset.connect(engineStr)

for t in db.tables:
    db[t].drop()

t = db['gebruikers']
for r in t:
    print(r)