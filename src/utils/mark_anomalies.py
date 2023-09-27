import pandas as pd


def mark_anomalies(data):
    # Inicialmente, todas as transações são consideradas normais (False)
    data["anomaly"] = False

    # Regras para detecção de anomalias
    failed_threshold = 1  # Limite para transações "failed"
    reversed_threshold = 1  # Limite para transações "reversed"
    denied_threshold = 1  # Limite para transações "denied"

    # Calcular a contagem de transações com base nas colunas de status e tempo
    data["count"] = 1  # Inicialmente, definimos todas as transações como 1
    data['time'] = pd.to_datetime(data['time'], format='%Hh %M')

    # Marcar transações como anomalias com base nas regras
    data.loc[
        (data["status"] == "failed") & (data["count"] > failed_threshold),
        "anomaly"
    ] = True
    data.loc[
        (data["status"] == "reversed") & (data["count"] > reversed_threshold),
        "anomaly"
    ] = True
    data.loc[
        (data["status"] == "denied") & (data["count"] > denied_threshold),
        "anomaly"
    ] = True

    # Retornar o DataFrame com as anomalias marcadas
    return data
