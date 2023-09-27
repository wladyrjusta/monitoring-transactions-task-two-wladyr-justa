import matplotlib.pyplot as plt
from io import BytesIO
import base64


def visualize_anomalies(data, title, description):
    # Extrair a parte da hora da coluna de datetime
    data['hour'] = data['time'].dt.hour

    # Criar uma nova coluna 'hourly' para representar a hora a cada intervalo
    # de 1 hora
    data['hourly'] = data['hour']

    # Pivotar a tabela para ter os status como colunas
    data_pivot = data.pivot_table(index='hourly', columns='status',
                                  values='count', aggfunc='sum').fillna(0)

    # Plote o gráfico de barras empilhadas com tamanho maior
    plt.figure(figsize=(16, 8))
    data_pivot.plot(kind='bar', stacked=True)
    plt.title(title)
    plt.xlabel('Hora do Dia (a cada 1 hora)')
    plt.ylabel('Contagem de Anomalias')
    plt.xticks(range(len(data_pivot.index)), data_pivot.index, rotation=45)
    plt.legend(title='Status')
    plt.grid(axis='y')

    # Salvar o gráfico como um arquivo temporário em formato PNG
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=150)
    buffer.seek(0)

    # Converter a imagem em base64
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Criar o conteúdo HTML com o gráfico e os metadados
    html_content = f"""
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <img src="data:image/png;base64,{image_base64}"
        alt="Gráfico de Anomalias">
        <h3>{description}</h3>
    </body>
    </html>
    """

    return html_content
