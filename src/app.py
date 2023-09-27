from flask import Flask
from controller.generate_graphics_html_controller import (
    generate_graphic_endpoint_anomalies_1,
    generate_graphic_endpoint_anomalies_2,
    detect_anomalies_endpoint_1,
    detect_anomalies_endpoint_2
)

app = Flask(__name__)


@app.route('/generate_graphic/transactions-anomalies-1')
def generate_graphic_route_anomalies_1():
    return generate_graphic_endpoint_anomalies_1()


@app.route('/generate_graphic/transactions-anomalies-2')
def generate_graphic_route_anomalies_2():
    return generate_graphic_endpoint_anomalies_2()


@app.route('/generate-alerts-1', methods=['GET'])
def generate_alerts_route_1():
    return detect_anomalies_endpoint_1()


@app.route('/generate-alerts-2', methods=['GET'])
def generate_alerts_route_2():
    return detect_anomalies_endpoint_2()


if __name__ == '__main__':
    app.run(debug=True)
