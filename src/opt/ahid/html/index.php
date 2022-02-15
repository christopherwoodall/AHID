<?php
#header("Content-Type: application/json");
header("Expires: on, 01 Jan 1970 00:00:00 GMT");
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");


if(isset($_POST['code'])){
  $frame = $_POST['code'];
  $width = $_POST['width'];
  $height = $_POST['height'];
  $x = $_POST['x'];
  $y = $_POST['y'];
  $script_path = dirname( __FILE__ );

  //$command = escapeshellcmd("$script_path/stream.py '$frame' $x $y $width $height");

  //$command = escapeshellcmd("$script_path/stream.py '$frame' $x $y $width $height");
  //$command = escapeshellcmd("$script_path/stream.py '$frame' 2>&1");

  //$frame_decoded = str_replace('-', '+', $frame);
  //$frame_decoded = str_replace('_', '/', $frame_decoded);

  $command = "$script_path/stream.py '$frame' 2>&1";
  echo $command;
  $output  = shell_exec($command);

  echo $output;

  exit;
}
?>
<!doctype html>

<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="A front-end template that helps you build fast, modern mobile web apps.">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0">
    <title>AHID</title>

    <link rel="stylesheet" href="/assets/css/style.css">
  </head>
  <body>
    <div class="row">
        <div class="aside col-2">
            <div class="logo">
                AHID
            </div>
            <div class="menu">
              <a href="#" id="start" class="btn green">
                Start Capture
              </a>
              <a href="#" id="stop" class="btn red">
                Stop Capture
              </a>
              <div id="stats" class="stats">
                <div class="stats-title">
                  Display Stats
                </div>
                <div class="stats-content">
                  <div class="stats-item">
                    <div class="stats-item-title">
                      Screen Width
                      <span id="screen-width">0</span>
                    </div>
                  </div>
                  <div class="stats-item">
                    <div class="stats-item-title">
                      Screen Height
                      <span id="screen-height">0</span>
                    </div>
                  </div>
                </div>
                <a href="#" id="update" class="btn">
                  Update
                </a>
              </div>
            </div>
        </div>

        <div class="content col-10">
          <div class="row">
          <div class="header col-12">Home</div>
          </div>
          <div class="row">
                <div class="col-4">
                  <div class="media">
                    <video id="video" width="800" height="680" autoplay></video>
                  </div>
                  <div class="media">
                    <canvas id="scrapped"></canvas>
                  </div>
                </div>
                <div class="col-8">
                  <div class="diagnostics" id="diagnostics">
                    <span>AHID v0.1</span>
                    <span>Diagnostic Data</span>
                  </div>
                </div>

          </div>
        </div>

    </div>

<script>
let width = screen.width;
let height = screen.height;
// move mouse to width, height
</script>
<script src="/assets/js/face-api.min.js"></script>
<script id="streamjs" src="/assets/js/stream.js"></script>

  </body>
</html>
<!--
https://itnext.io/face-api-js-javascript-api-for-face-recognition-in-the-browser-with-tensorflow-js-bcc2a6c4cf07
https://github.com/justadudewhohacks/face-recognition.js#how-to-use
-->