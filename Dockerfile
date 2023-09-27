FROM mysql:8.0.32

# Definindo a senha do root do MySQL
ENV MYSQL_ROOT_PASSWORD=A5bR8tL1pX9

# Cria um banco de dados
ENV MYSQL_DATABASE=transactions_monitoring

# Copia os arquivos CSV para a pasta permitida
COPY transactions_1.csv /var/lib/mysql-files/
COPY transactions_2.csv /var/lib/mysql-files/

# Copia os scripts SQL para o diretório de inicialização
COPY create_table.sql /docker-entrypoint-initdb.d/
COPY load_data.sql /docker-entrypoint-initdb.d/

