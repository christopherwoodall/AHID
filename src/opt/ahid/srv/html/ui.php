<?php
#header("Content-Type: application/json");
header("Expires: on, 01 Jan 1970 00:00:00 GMT");
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");


if(isset($_POST['code'])){
  $frame = $_POST['code'];
  $script_path = dirname( __FILE__ );
  $command = escapeshellcmd("$script_path/stream.py '$frame'");
  $output  = shell_exec($command);

  echo 'ok';

  exit;
}
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AHID</title>
  </head>

  <body class="grey darken-3">

    <!--<script id="streamjs" src="/assets/js/stream.js"></script>-->
  </body>
</html>