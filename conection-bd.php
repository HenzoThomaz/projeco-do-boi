<?php

$servername = "localhost";
$username = "root";
$password = "";
$dbname = "projeto-boi";

// aqui serve para criar a conexão com o banco de dados do xampp

$conn = new mysqli(hostname: $servername, username: $username, password: $password, database: $dbname);


// verificação de conexão

if ($conn->connect_error ) {
    die("Conexão falhou: ". $conn->connect_error);
}
echo "Conectado com sucesso!";

?>