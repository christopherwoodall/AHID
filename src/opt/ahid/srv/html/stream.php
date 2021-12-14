<?php

$frame = $_POST['code'];
$script_path = dirname( __FILE__ );
$command = escapeshellcmd("$script_path/stream.py '$frame'");
$output  = shell_exec($command);

echo 'ok';
