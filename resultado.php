<?php
    session_start();
    $dados = $_SESSION["dados"];
    $autor = $_GET["autor"];
    $nota = $dados[1];
    $rank = $dados[2];
    $similares = $dados[3];
    $media_nota_similares = $dados[4];
    $media_rank_similares = $dados[5];
    $titulo = $dados[6];
    $url = $dados[7];
    $links = $dados[8];
    $titulos = $dados[9];
    $sites = $dados[10];
    $alternativos = [$links, $titulos, $sites];
?>

<html>
    <head>
        <title></title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="css/verificacao.css">
    </head>
    <body>
        <div class="container">
            <div class="border p-4 mt-4 rounded bg-white">
                <div class="text-center">
                    <strong><a href="<?php echo $url?>" class="titulo text-primary"><?php echo $titulo; ?></a></strong>
                    <hr>
                    <div class="text-success mt-3 d-none">
                        <div class="border ml-auto mr-auto mb-3 border-success rounded-circle d-flex align-items-center justify-content-center pontuacao">
                            <h1 style="font-size: 4em;" class="m-0 p-0">83</h1>
                        </div>
                        <div class="progress mb-3 mr-auto ml-auto d-none d-md-flex" style="width: 500px; height: 12px;">
                            <div class="progress-bar bg-success" role="progressbar" style="width: 83%" aria-valuenow="83" aria-valuemin="0" aria-valuemax="100"></div>
                        </div>
                        <p><strong>Esta notícia é confiável!</strong></p>
                    </div>
                    <p class="d-none">Sinta-se a vontade para compartilhar com seus amigos!</p>
                </div>

                <div class="ml-2 mr-2 mt-5">
                    <table class="table table-striped table-bordered">
                        <tbody>
                            <tr>
                                <th scope="row">Autor</th>
                                <th scope="row">Nota</th>
                                <th scope="row">Rank</th>
                                <th scope="row">Similares</th>
                                <th scope="row">Media nota similares</th>
                                <th scope="row">Media rank similares</th>
                            </tr>
                            <tr>
                                <td><?php echo $autor ?></td>
                                <td><?php echo $nota ?></td>
                                <td><?php echo $rank ?></td>
                                <td><?php echo $similares ?></td>
                                <td><?php echo $media_nota_similares ?></td>
                                <td><?php echo $media_rank_similares ?></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="text-left border rounded pt-0 ml-2 mr-2 mt-5 mb-4">
                    <div class="bg-cinza mt-0 pt-3 pb-1 pl-3 pr-3">
                        <strong>Fontes alternativas</strong>
                        <p>Veja aqui alguns sites que publicaram esta mesma notícia</p>
                    </div>
                    <div class="pl-md-3 pr-md-3 pb-md-3">
                        <?php for($i = 0; $i < sizeof($sites); $i++){ ?>
                            <div class="mt-3 w-100">
                                <strong><?php echo $alternativos[2][$i] ?></strong><br>
                                <a href="<?php echo $alternativos[0][$i]; ?>"><?php echo $alternativos[1][$i]; ?></a>
                            </div>
                            <?php if($i != sizeof($sites) - 1){ ?> <hr> <?php } ?>
                        <?php } ?>
                    </div>
                </div>
                <div class="text-right mt-5">
                    <a href="#" class="btn btn-danger d-none">Não concordo</a>
                    <a href="index.html" class="btn btn-success">Voltar</a>
                </div>
            </div>
        </div>

        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    </body>
</html>
