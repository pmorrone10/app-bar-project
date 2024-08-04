# BAR APP

### Levantar aplicaciones

    Ejecutar el comando ``docker-compose up -d``

## Backend

### Tests

    Para ejecutar los test pararse sobre la carpeta backend y escribir el comando:
     - make init
     - make test

### Curl de prueba

    curl --location 'http://localhost:8080/api/v1/order/1' -> 200 OK
    curl --location 'http://localhost:8080/api/v1/order/2' -> 404 Not Found

## Frontend

### Tests

    Para ejecutar los test pararse sobre la carpeta frontend y escribir el comando:
     - npm install
     - npm test

### Request de prueba

    curl --location 'http://localhost:3000/order/1' -> 200 OK
