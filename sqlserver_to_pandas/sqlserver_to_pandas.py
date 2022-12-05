import pandas as pd
from sqlalchemy import create_engine

# Se recomienda utilizar un archivo .env con las variables y datos
# sensibles como nombres de usuarios, contraseñas u otra información.
username = USERNAME
password = PASSWORD
hostname = HOSTNAME
port = PORT
database = DATABASE
driver = 'ODBC+Driver+17+for+SQL+Server'

# Creamos la URL de conexión
cnx_url = f'mssql+pyodbc://{username}:{password}@{server}:{port}/{database}?driver={driver}'

# Creamos el SQLAlchemy Engine
engine = create_engine(cnx_url)

# Consulta de SQL
sql_str = 'SELECT * FROM table_name WHERE conditions'

# Realizamos la consulta directamente con pandas
df = pd.read_sql(sql_str, engine)
