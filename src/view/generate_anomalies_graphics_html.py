import schedule
import time
from model.load_transactions_data import load_data_transactions
from utils.mark_anomalies import mark_anomalies
from utils.visualize_anomalies import visualize_anomalies
from utils.generate_alert_recommendation import generate_alert_recommendation

DESCRIPTION = (
    "Esta tabela exibe a contagem de anomalias ao longo do tempo, agrupada por"
    + " hora do dia.\n Cada linha representa uma hora do dia, e as colunas "
    + "correspondem aos diferentes estados ou 'status' das anomalias.\n"
    "A altura das barras em cada hora representa o número de ocorrências de "
    + "cada tipo de anomalia naquela hora específica.\n"
    + "O gráfico de barras empilhadas permite visualizar a distribuição das"
    + " anomalias ao longo das horas, destacando\n"
    + "as proporções relativas de cada tipo de anomalia em um determinado "
    + "momento do dia.\n Isso facilita a identificação de tendências ou"
    + " padrões de anomalias em diferentes momentos."
)


def generate_anomalies_graphics_html_transactions_1():
    transactions_1 = load_data_transactions('transactions_1')

    anomalies_1 = mark_anomalies(transactions_1)

    html_content_anomalies_transactions_1 = visualize_anomalies(
        anomalies_1, title="Gráfico Transaões e Anomalias",
        description=DESCRIPTION
    )
    return html_content_anomalies_transactions_1


def generate_anomalies_graphics_html_transactions_2():
    transactions_2 = load_data_transactions('transactions_2')
    anomalies_2 = mark_anomalies(transactions_2)

    html_content_anomalies_transactions_2 = visualize_anomalies(
        anomalies_2, title="Gráfico Transaões e Anomalias",
        description=DESCRIPTION
    )
    return html_content_anomalies_transactions_2


def generate_anomalies_alerts_1():
    transactions_1 = load_data_transactions('transactions_1')
    anomalies_1 = mark_anomalies(transactions_1)
    alerts_1 = generate_alert_recommendation(anomalies_1)
    return alerts_1


def generate_anomalies_alerts_2():
    transactions_2 = load_data_transactions('transactions_2')
    print(transactions_2)
    anomalies_2 = mark_anomalies(transactions_2)
    print(anomalies_2)
    alerts_2 = generate_alert_recommendation(anomalies_2)
    return alerts_2


def run_scheduled_tasks():
    while True:
        schedule.run_pending()
        time.sleep(1)


# Agendar as funções para rodar a cada hora
schedule.every().hour.do(generate_anomalies_graphics_html_transactions_1)
schedule.every().hour.do(generate_anomalies_graphics_html_transactions_2)
schedule.every().hour.do(generate_anomalies_alerts_1)
schedule.every().hour.do(generate_anomalies_alerts_2)

# Iniciar a execução das tarefas agendadas
if __name__ == "__main__":
    run_scheduled_tasks()
