//"use strict";

// GLOBAL
var last_x = 0,
    last_y = 0;

// CONST

const video = document.getElementById("video");
const start = document.getElementById("start");
const stop = document.getElementById("stop");

var canvas    = document.getElementById("scrap");
canvas.width  = 500; //window.innerWidth;
canvas.height = 500; //window.innerHeight;


////////////////////////////////////////////////////////////////////////////////
// STATS AND DIAGNOSTICS
var screen_width_elem  = document.getElementById('screen-width'),
    screen_height_elem = document.getElementById('screen-height');
screen_width_elem.textContent  = screen.width;
screen_height_elem.textContent = screen.height;


let Terminal = class {
  constructor() {
    this.elem = document.getElementById('diagnostics');
  }
  print(text) {
    const span = document.createElement('span');
    span.textContent = text;
    this.elem.appendChild(span);
  }
}
////////////////////////////////////////////////////////////////////////////////

////////////////////////////////////////////////////////////////////////////////
// Image encoding
function encode(buffer) {
  return buffer
    .replace(/\+/g, '-') // Convert '+' to '-'
    .replace(/\//g, '_') // Convert '/' to '_'
    //.replace(/=+$/, ''); // Remove ending '='

}

function decode(buffer) {
  return buffer
    .replace(/-/g, '+') // Convert '+' to '-'
    .replace(/_/g, '/') // Convert '/' to '_'
    //.replace(/=+$/, ''); // Remove ending '='

}


////////////////////////////////////////////////////////////////////////////////

function send(code) {
  var content = {
        'image': code,
        width: screen.width,
        height: screen.height,
        x: last_x,
        y: last_y
      },
      post_data = JSON.stringify(content);
      //post_data = Object.entries(content).map(([k,v])=>{return k+'='+v}).join('&');
  fetch(`/`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode:   'no-cors', // no-cors, *cors, same-origin
      cache:  'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      headers: {
        //"Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
        "Content-type": "application/json; charset=UTF-8"
      },
      body: post_data
    })
  //.then(response => response.json())
  .then(response => response.text())
  .then(data => {
    let term = new Terminal();
    term.print('Target Acquired');
    //last_x = data.split(',')[0];
    //last_y = data.split(',')[1];

    var image = document.getElementById('scrapped');
    image.src = `data:image/png;base64,${decode(data)}`;
  });

}


////////////////////////////////////////////////////////////////////////////////
//https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL

let scrapper = null;
let scrap = () => {
  var context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  //image_data = canvas.toDataURL("image/png", 0.25).split(';base64,')[1];
  image_data = canvas.toDataURL().split(';base64,')[1];
  encoded_data = encodeURIComponent(image_data);
  send(encoded_data);
  //send(image_data);
}

////////////////////////////////////////////////////////////////////////////////



function main() {
    var displayMediaOptions = {
      video: {
        cursor: "always",
      },
      audio: false,
    };

    start.onclick = function (e) {
      startSharing();
    };
    stop.onclick = function (e) {
      window.clearInterval(scrapper);
      stopSharing();
    };

    async function startSharing() {
        try {
          navigator.mediaDevices.getDisplayMedia(displayMediaOptions).then(
            (stream) => {
              video.srcObject = stream;

              scrapper = window.setInterval(scrap, 6000);
            },
            (err) => {
              console.error(err)
            }
          );
        } catch (error) {
          console.log(error);
        }
    }

      function stopSharing() {
        let tracks = video.srcObject.getTracks();
        tracks.forEach((track) => track.stop());
        video.srcObject = null;
      }
  }


  main();




// Reload JS
/*
var button = document.getElementById('reload');
button.addEventListener('click', handler, false);
function handler() {
  var old_script = document.getElementById('streamjs'),
      new_script = document.createElement('script');

  old_script.remove();

  new_script.setAttribute('type', 'text/javascript');
  new_script.setAttribute('src',  '/assets/js/stream.js');
  new_script.setAttribute('id',   'streamjs');
  new_script.setAttribute('async','true');
  document.head.appendChild(new_script);
}
*/
//
