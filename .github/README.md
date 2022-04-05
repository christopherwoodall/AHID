<p>
  <br>
  <h1 align="center">
    <a href="https://github.com/christopherwoodall/AHID">
      AHID
    </a>
  </h1>
  <h3 align="center">
    Under Construction
  </h3>
</p>

<h4 align="center">Hardware based, AI assisted, Automated Human Input Device</h4>

<p align="center">
  <a href="#about">About</a> •
    <a href="#process">Process</a> •
  <a href="#installation">Installation</a> •
  <a href="#demo">Demo</a>
</p>

## About

AHID utilizes a Raspberry Pi(4/Zero) and the Linux Kernel [USB Gadget Module](https://www.kernel.org/doc/html/v4.19/driver-api/usb/gadget.html) to simulate user input and off load tasks to an external compute device; think Game Shark.

As the streaming(ala Twitch.tv) and the gaming market grow, so to does the market share of people looking for an edge. The edge people are looking for comes in may forms- be it a gaming chair, or better monitor- but all too often the quick fix is cheating.

As cheats become more complex so do the client side anti-cheats, this dichotomy has left us in a race to a race to ring zero; who can hook the kernel first. This proof of concept bypasses the host kernel altogether(by not running on the host device), preventing most anti-cheats from being able to detect any malfeasance.

Possible use cases may include:
  - Undetectable cheats; e.g. aimbot, auto farming, etc.
  - Mimic repetative user interaction.


## Process
  1. A web server running on the Raspberry Pi serves a simple webpage.
  2. This webpage makes use of the Javascript [Media Capture and Stream API](https://developer.mozilla.org/en-US/docs/Web/API/Media_Streams_API) to capture game feeds
  3. These feeds are then sent to Pi over a REST API.
  4. The Pi then processes the stream using image recgonition/machine learning to identify key elements.
  5. Based on the above processing, keyboard/mouse movements are emulated; making it appear as if a human is interacting with the application.



## Installation
**TO DO**


# Demo
![Example](docs/test.png?raw=true "Screenshot")

