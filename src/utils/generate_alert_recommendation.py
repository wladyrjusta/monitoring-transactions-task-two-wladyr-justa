# Esta função gera uma recomendação de alerta
# com base nas anomalias detectadas no DataFrame de dados.
# Se não houver anomalias, ela retornará uma mensagem
# informando que não foram detectadas anomalias.
# Caso contrário, ela retornará uma mensagem indicando
# que anomalias foram detectadas e que é necessário verificar os detalhes.


def generate_alert_recommendation(data):
    # Filtrar as anomalias no DataFrame
    anomalies = data[data["anomaly"]]

    if anomalies.empty:
        return "Não há anomalias detectadas nas transações."
    else:
        # Inicializar uma lista para armazenar os alertas específicos
        alerts = []

        # Iterar sobre as anomalias e gerar alertas específicos
        for index, row in anomalies.iterrows():
            anomaly_type = row["status"]  # Tipo de anomalia (status)
            timestamp = row["time"]  # Momento da anomalia
            alert = (
                f"Anomalia do tipo '{anomaly_type}' detectada às {timestamp}."
            )
            alerts.append(alert)

        # Retornar os alertas específicos como uma lista de strings
        return alerts
