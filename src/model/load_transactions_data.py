from model.execute_sql_querie import execute_query_and_get_dataframe
from database.get_mysql_connection import get_mysql_connection

# Obtém a conexão com o banco de dados
CONNECTOR = get_mysql_connection()


def load_data_transactions(table_name):

    # Crie e execute as consultas para cada tabela
    data_frame_transactions = execute_query_and_get_dataframe(
        CONNECTOR, f"SELECT * FROM {table_name}", table_name
    )

    return data_frame_transactions
