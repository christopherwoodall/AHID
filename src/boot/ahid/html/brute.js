
codes = document.getElementById('codes');
code_elems = [ ]
active = 0

for (const [index, code] of code_list.entries()) {
    let element = document.createElement('li');
    element.innerHTML = code;
    element.dataset.index = index;
    element.addEventListener('click', (e) => {
        select(e.target.dataset.index);
    });
    code_elems.push(element);
    codes.appendChild(element);
}


/*********************************************************** */

function send(code) {
    fetch(`/input.php?code=${code}`)
    .then(response => response.json())
    .then(data => console.log(data));
}


function unlock() {
    send('unlock');
}

function select(index) {
    code_elems[active].classList.remove('active');
    active = parseInt(index);
    target = code_elems[active];
    target.classList.add('active');
    send(target.textContent);
}

function start() {
    target = code_elems[active];
    target.classList.add('active');
    send(target.textContent);
}

function next() {
    if (active < code_elems.length - 1) {
        code_elems[active].classList.remove('active');
        active += 1;
        target = code_elems[active];
        target.classList.add('active');
        send(target.textContent);
    }
}


/*********************************************************** */

