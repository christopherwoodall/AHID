const video = document.getElementById("video");
const start = document.getElementById("start");
const stop = document.getElementById("stop");

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
      stopSharing();
    };



    async function startSharing() {
        try {
            //video.srcObject = await navigator.mediaDevices.getDisplayMedia(
            /*
            navigator.mediaDevices.getDisplayMedia(displayMediaOptions).then((stream)=>
            {
                video.srcObject = stream;
            }, (err)=> console.error(err)
            );
            */
            navigator.mediaDevices.getUserMedia({video: {}}) .then((stream)=> {video.srcObject = stream;}, (err)=> console.error(`ERROR: ${err}`));
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
