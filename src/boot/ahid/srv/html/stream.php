<?php

if(isset($_POST['code'])){

    $request = $_POST['code'];
    #$command = escapeshellcmd("/var/www/html/stream.py $request");
    #$output  = shell_exec($command);
    $output  = passthru("python stream.py test");
    #echo $request;
    echo $output;

    #$debuglog = fopen("/var/www/html/php-debug.txt", "w");
    #fwrite($debuglog, $request);
    #fclose($debuglog);

    exit;
}

