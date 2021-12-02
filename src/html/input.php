<?php

if(isset($_GET['code'])){
    $request = $_GET['code'];



    $command = escapeshellcmd("/var/www/html/input.py $request");
    $output = shell_exec($command);
    #echo $output;

    echo json_encode($request);

    exit;
}

