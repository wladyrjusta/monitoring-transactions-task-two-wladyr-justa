<h1>Monitoring Transactions App</h1>

<p>Este é um aplicativo que monitora transações e gera gráficos com anomalias encontradas por hora. A aplicação é configurada para ser executada em um contêiner Docker.</p>

<h2>Pré-requisitos</h2>

<p>Certifique-se de ter o seguinte instalado no seu sistema:</p>
<ul>
    <li>Docker: <a href="https://docs.docker.com/get-docker/">Instalação do Docker</a></li>
    <li>Python 3.x: <a href="https://www.python.org/downloads/">Instalação do Python</a></li>
</ul>

<ol>
    <li>Clone o repositório do projeto:</li>
</ol>

<pre><code>git clone git@github.com:wladyrjusta/monitoring-transactions-task-two-wladyr-justa.git</code></pre>

<ol>
    <li>Navegue até o diretório do projeto:</li>
</ol>

<pre><code>cd monitoring-transactions-task-two-wladyr-justa</code></pre>

<h2>Criando um Ambiente Virtual (Recomendado)</h2>

<p>Recomendamos que você crie e ative um ambiente virtual Python antes de instalar as dependências. Isso ajuda a isolar as dependências do projeto e evita conflitos com outras versões de pacotes Python instalados globalmente no seu sistema. Siga estas etapas:</p>

<ol>
    <li>Crie um novo ambiente virtual:</li>
</ol>

<pre><code>python -m venv venv</code></pre>

<p>OU</p>

<pre><code>python3 -m venv venv</code></pre>

<ol>
    <li>Ative o ambiente virtual (no Windows):</li>
</ol>

<pre><code>venv\Scripts\activate</code></pre>

<p>Ou ative o ambiente virtual (no macOS e Linux):</p>

<pre><code>source venv/bin/activate</code></pre>

<p>Depois de ativar o ambiente virtual, seu terminal deve mostrar o nome do ambiente entre parênteses, indicando que está ativo.</p>

<h2>Configuração do Contêiner Docker</h2>

<p>Este aplicativo usa um contêiner Docker para executar um servidor MySQL. Siga estas etapas para configurar o contêiner:</p>

<ol>
    <li>Crie o contêiner Docker com o seguinte comando:</li>
</ol>

<pre><code>docker build -t sales-monitoring-app .</code></pre>

<ol>
    <li>Execute o contêiner Docker:</li>
</ol>

<pre><code>docker run -d -p 3306:3306 --name sales-monitoring-container sales-monitoring-app</code></pre>

<p>Isso iniciará o servidor MySQL em um contêiner Docker. O servidor MySQL será acessível na porta 3306.</p>

<h2>Executando o Aplicativo</h2>

<ol>
    <li>Instale as dependências Python:</li>
</ol>

<pre><code>pip install -r requirements.txt</code></pre>

<ol>
    <li>Inicie o aplicativo Flask:</li>
</ol>

<pre><code>python app.py</code></pre>

<p>O aplicativo estará acessível em:</p>

<ul>
    <li>Página com gráficos da "transactions-anomalies-1": <a href="http://localhost:5000/generate_graphic/transactions-anomalies-1">http://localhost:5000/generate_graphic/transactions-anomalies-1</a></li>
    <li>Página com gráficos da "transactions-anomalies-2": <a href="http://localhost:5000/generate_graphic/transactions-anomalies-2">http://localhost:5000/generate_graphic/transactions-anomalies-1</a></li>
</ul>

<h2>Explorando os Dados</h2>

<p>O sistema monitora transações em tempo real, alertando automaticamente quando ocorrem negações, reversões ou falhas.</p>

<p>Além disso, gera gráficos em HTML que mostram o volume de transações por hora e o número de transações fracassadas por hora, acessíveis por meio de um endpoint específico.</p>

<p>Isso garante um monitoramento eficaz e uma resposta imediata a qualquer anomalia."</p>

</body>
</html>
