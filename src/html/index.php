<?php

/*
  Inspiration:
    - https://codepen.io/themustafaomar/pen/jLMPKm
  */
?>

<!DOCTYPE html>
<html>
  <head>
      <title>Pusher - Rust Code Lock Raiding</title>

      <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">

  </head>

  <body class="grey darken-3">
    <!--- Navbar --->
    <nav class="deep-purple lighten-1">
      <div class="nav-wrapper">
        <a href="#" class="brand-logo">Pusher</a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><a href="#">###</a></li>
          <li><a href="#">###</a></li>
          <li><a href="#">###</a></li>
        </ul>
      </div>
    </nav>
    <!-- /Navbar -->

    <!--
    <div class="row">
      <div class="col s2 grey darken-2">
        <a class="waves-effect waves-light btn-large grey darken-1 col s12">Sessions</a>
        <br><br>
        <a class="waves-effect waves-light btn-large grey darken-1 col s12">Settings</a>
      </div>
      <div class="col s10">

        <div class="row">
          <div class="col s12 grey darken-2">
          <a class="waves-effect waves-light btn-large"
               onclick="start()">
              Start
            </a>
            <a class="waves-effect waves-light btn-large"
               onclick="next()">
              Next
            </a>
            <a class="waves-effect waves-light btn-large">Stop</a>
          </div>
        </div>

        <div class="row">
          <div class="col s2 grey darken-2">
            <div>CODES</div>
            <style>
              .active {
                background-color: #e0e0e0;
              }
              ol { list-style: none; }
            </style>
            <ol id="codes"></ol>
          </div>
          <div class="col s10 grey darken-2">CONTENT</div>
        </div>

      </div>
    </div>
    -->


    <div class="row">
      <div class="row">
        <div class="col s12 grey darken-2">
          <a class="waves-effect waves-light btn-large"
              onclick="start()">
            Start
          </a>
          <a class="waves-effect waves-light btn-large"
              onclick="next()">
            Next
          </a>
          <a class="waves-effect waves-light btn-large"
             onclick="unlock()">
            Unlock
          </a>
        </div>
      </div>

      <div class="row">
        <div class="col s12 grey darken-2">
          <div>CODES</div>
          <style>
            .active { background-color: #e0e0e0; }
            ol {
              overflow-y: scroll;
              height: 75vh;
            }
          </style>
          <ol id="codes"></ol>
        </div>
      </div>


    <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>

    <script src="/codes.js"></script>
    <script src="/brute.js"></script>
  </body>
</html>