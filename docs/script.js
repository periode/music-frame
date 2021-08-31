let audio_rd, log, timeout_rd
let audios_pp
let samples_rd = [
    "vexations/0.mp3",
    "vexations/1.mp3",
    "vexations/2.mp3",
    "vexations/3.mp3",
    "vexations/4.mp3",
    "vexations/5.mp3"
]
let index_rd = 0
let duration_rd

let silence_min = 1000
let silence_max = 5000

let startAudio = (_el, _mode) => {
    if (_el.innerText === 'stop') {
        stopAudio()
        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `stopped.`
        log.prepend(el)
        _el.innerText = 'play'
        return;
    }

    _el.innerText = 'stop'
    console.log(_mode);

    switch (_mode) {
        case 'random':
            startRandomDelayed()
            break;
        case 'polyphonic':
            startPolyphonic();
            break;
        default:
            console.log("wrong playmode")
            break;
    }
}

let stopAudio = () => {
    if (audio_rd) audio_rd.pause()
    if(audios_pp[0]) audios_pp[0].pause()
    if (timeout_rd) clearTimeout(timeout_rd)
}

let startRandomDelayed = () => {
    audio_rd = document.getElementById('random-delayed')
    log = document.getElementById('log-rd')
    playRandomDelayed()
}

let playRandomDelayed = () => {
    index_rd = Math.floor(Math.random() * samples_rd.length)
    audio_rd.src = `assets/audio/${samples_rd[index_rd]}`
    audio_rd.onloadedmetadata = () => {
        audio_rd.play()

        let offset = audio_rd.duration * 1000 + Math.random() * silence_max + silence_min

        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `playing ${samples_rd[index_rd]}, waiting ${Math.floor(offset / 1000)} seconds before next play...`
        log.prepend(el)
        if (timeout_rd) clearInterval(timeout_rd)
        timeout_rd = setTimeout(playRandomDelayed, offset)
    }
}

let startPolyphonic = () => {
    audios_pp = document.getElementsByClassName('polyphonic')
    log = document.getElementById('log-pp')
    playPolyphonic()
}

let playPolyphonic = () => {
    audios_pp[0].loop = true
    audios_pp[0].src = 'assets/audio/swirl/full.mp3'
    audios_pp[0].onloadedmetadata = () => {
audios_pp[0].play()
        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += 'playing mixed-down version of the composition'
log.prepend(el)
    }
}