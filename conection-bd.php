<?php

$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "projeto-boi";
$port = 3306; 

// aqui serve para criar a conexão com o banco de dados do xampp

$conn = new mysqli(hostname: $servername, username: $username, password: $password, database: $dbname, port:$port);


// verificação de conexão

if ($conn->connect_error ) {
    die("Conexão falhou: ". $conn->connect_error);
}
echo "Conectado com sucesso!";

?>