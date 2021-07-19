Airflow server with simple example

In order to run follow steps:
1. run prepare.sh
2. in terminal run: docker-compose up airflow-init
3. then run: docker-compose up

In order to access web-server: http://localhost:8080

In order to run dag in web manually: run dag named yfinance_daily_analisys

In order to stop and delete all redundant data run in terminal: docker-compose down --volumes --rmi all