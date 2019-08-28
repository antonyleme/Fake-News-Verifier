<?php
    $url = $_GET["url"];
    $dados = json_decode(exec("python algoritmo/main.py {$url}"), true);
    $autor = $dados[0];
    $nota = $dados[1];
    $rank = $dados[2];
    $similares = $dados[3];
    $media_nota_similares = $dados[4];
    $media_rank_similares = $dados[5];

    echo "{$autor} {$nota} {$rank} {$similares} {$media_nota_similares} {$media_rank_similares}";
?>
