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

    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
  </head>

  <body class="grey darken-3">
    <!--- Navbar --->
    <nav class="deep-purple lighten-1">
      <div class="nav-wrapper">
        <a href="#" class="brand-logo" style="padding-left:1em;">
          AHID
        </a>
        <!--
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><a href="#">###</a></li>
          <li><a href="#">###</a></li>
          <li><a href="#">###</a></li>
        </ul>
        -->
      </div>
    </nav>
    <!-- /Navbar -->

    <div class="row">
      <div class="row">
        <div class="col s12 grey darken-2">
          <a class="waves-effect waves-light btn-large"
              id="start">
            Start Capture
          </a>
          <a class="waves-effect waves-light btn-large"
              id="stop">
            Stop Capture
          </a>
        </div>
      </div>

      <div class="row grey darken-4">
        <div class="col s2">
          Screen width:
          Screen height:
        </div>

        <div class="col s10 grey darken-2">

<video id="video" width="800" height="680" autoplay></video>
<canvas id="scrapped"></canvas>

        </div>
      </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

    <script id="streamjs" src="/assets/js/stream.js"></script>
  </body>
</html>