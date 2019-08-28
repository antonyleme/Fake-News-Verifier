<?php 
    $url = $_GET["url"]; 
    $dados = json_decode(exec("python algoritmo/main.py {$url}"), true);
    var_dump($dados);
?>