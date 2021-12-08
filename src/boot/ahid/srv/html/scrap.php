<?php
#header("Content-Type: application/json");
header("Expires: on, 01 Jan 1970 00:00:00 GMT");
header("Last-Modified: " . gmdate("D, d M Y H:i:s") . " GMT");
header("Cache-Control: no-store, no-cache, must-revalidate");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Screen Share</title>
</head>
<body align="center">
  <h2>Screen Capture</h2>
  <p>
    <button id="start">Start Sharing</button>
    <button id="stop">Stop Sharing</button>
  </p>
  <video id="video" width="800" height="680" autoplay></video>
  <script src="/assets/js/script.js"></script>
</body>
</html>


