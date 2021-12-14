const video = document.getElementById("video");
const start = document.getElementById("start");
const stop = document.getElementById("stop");


//

function send(code) {
  var content = {'code': code},
      post_data = `code=${code}`;
      post_data = Object.entries(content).map(([k,v])=>{return k+'='+v}).join('&');
  fetch(`/stream/stream.php`, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode:   'no-cors', // no-cors, *cors, same-origin
      cache:   'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      headers: {
        "Content-type": "application/x-www-form-urlencoded; charset=UTF-8"
      },
      body: post_data
    })
  //.then(response => response.json())
  .then(response => response.text())
  .then(data => console.log(data));

}


////////////////////////////////////////////////////////////////////////////////
// Image encoding
function encode(buffer) {
  return buffer
    .replace(/\+/g, '-') // Convert '+' to '-'
    .replace(/\//g, '_') // Convert '/' to '_'
    //.replace(/=+$/, ''); // Remove ending '='

}

//https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
var canvas    = document.getElementById("scrapped");
canvas.width  = 500; //window.innerWidth;
canvas.height = 500; //window.innerHeight;
let scrapper = null;
let scrap = () => {
  var context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  //image_data = canvas.toDataURL("image/png", 0.5).split(';base64,')[1];
  image_data = canvas.toDataURL().split(';base64,')[1];
  encoded_data = encodeURIComponent(image_data);
  send(encoded_data);
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

