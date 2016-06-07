# How to connect to a PostgreSQL database using python & sqlalchemy

from scqlalchemy import create_engine

# dialect+driver://username:password@host:port/database
dialect = 'postgresql'
driver = 'pg800'
username = 'sysadmin'
password = '<password>'
host = 'localhost'
port = '5432'
database = 'kenamju'
baseStr = "{}+{}://{}:{}@{}:{}/{}"
engineStr = baseStr.format(dialect, driver, username, password, host, port, database)
print(engineStr)
