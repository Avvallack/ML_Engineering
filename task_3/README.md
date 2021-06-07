# ML-Flow docker compose
## Description
This service will create a containerized ml-flow server and run simple app and push the results of it work to server
## Content
- Ml-flow web server
- Nginx server to forward request from web to web server
- MYSQL database for store runs
- S3 bucket for artifact storage
## How to run
- In order to run the compose file you need to create .env file with following content:
    1. AWS_ACCESS_KEY_ID
    2. AWS_SECRET_ACCESS_KEY
    3. AWS_DEFAULT_REGION
    4. MYSQL_USER
    5. MYSQL_DATABASE
    6. MYSQL_PASSWORD
    7. MYSQL_ROOT_PASSWORD
- then run the command: docker-compose up -d --build