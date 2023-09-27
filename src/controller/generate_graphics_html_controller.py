from flask import Flask, jsonify
from view.generate_anomalies_graphics_html import (
    generate_anomalies_graphics_html_transactions_1,
    generate_anomalies_graphics_html_transactions_2,
    generate_anomalies_alerts_1,
    generate_anomalies_alerts_2
)
from flask import Response

app = Flask(__name__)


@app.route('/generate_graphic/transactions-anomalies-1')
def generate_graphic_endpoint_anomalies_1():
    html_graphic = generate_anomalies_graphics_html_transactions_1()

    return Response(html_graphic.encode('utf-8'),
                    content_type='text/html; charset=utf-8')


@app.route('/generate_graphic/transactions-anomalies-2')
def generate_graphic_endpoint_anomalies_2():
    html_graphic = generate_anomalies_graphics_html_transactions_2()

    return Response(html_graphic.encode('utf-8'),
                    content_type='text/html; charset=utf-8')


@app.route('/generate-alerts-1', methods=['POST'])
def detect_anomalies_endpoint_1():
    try:
        # Chame a função para gerar alertas
        alerts = generate_anomalies_alerts_1()

        # Verifique se há alertas
        if alerts:
            response_data = {
                "success": True,
                "alerts": alerts
            }
            return jsonify(response_data), 200
        else:
            response_data = {
                "success": True,
                "message": "Não foram encontradas anomalias."
            }
            return jsonify(response_data), 200
    except Exception as e:
        # Em caso de erro, retorne uma resposta de erro
        response_data = {
            "success": False,
            "error": str(e)
        }
        return jsonify(response_data), 500


@app.route('/generate-alerts-2', methods=['POST'])
def detect_anomalies_endpoint_2():
    try:
        # Chame a função para gerar alertas
        alerts = generate_anomalies_alerts_2()

        # Verifique se há alertas
        if alerts:
            response_data = {
                "success": True,
                "alerts": alerts
            }
            return jsonify(response_data), 200
        else:
            response_data = {
                "success": True,
                "message": "Não foram encontradas anomalias."
            }
            return jsonify(response_data), 200
    except Exception as e:
        # Em caso de erro, retorne uma resposta de erro
        response_data = {
            "success": False,
            "error": str(e)
        }
        return jsonify(response_data), 500


if __name__ == '__main__':
    app.run(debug=True)
