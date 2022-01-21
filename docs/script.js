let audio_rd, log, timeout_rd
let audios_pp, timeouts_pp = []


let index_rd = 0

let samples_pp = ["pad", "saba", "strumboli", "tree"]
let samples_max_pp = [2, 9, 10, 3]
let indexes_pp = [0, 0, 0, 0]

let silence_min = 1000
let silence_max = 5000
let volumes_timeout

let startAudio = (_el, _mode) => {
    stopAudio()
    if (_el.innerText === 'stop') {
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
        case 'oscillation':
            startOscillation();
            break;
        default:
            console.log("wrong playmode")
            break;
    }
}

let stopAudio = () => {
    if (audio_rd) audio_rd.pause()
    if (timeout_rd) clearTimeout(timeout_rd)
    if (timeouts_pp) for (let t of timeouts_pp) { clearTimeout(t) }
    if (volumes_timeout) clearTimeout(volumes_timeout)
    if (log) log = null

    document.querySelectorAll('audio').forEach(audio => {
        audio.pause()
    })
}

let audios_osc

let offsets = [
    Math.random()*0.0003,
    Math.random()*0.0003,
    Math.random()*0.0003,
    Math.random()*0.0003
]

let periods = [
    Math.random()*10+5,
    Math.random()*10+5,
    Math.random()*10+5,
    Math.random()*10+5,
]

let setVolumes = () => {
    for (let i = 0; i < audios_osc.length; i++) {
        let vol = (Math.sin(Date.now() * offsets[i] + periods[i]) + 1) / 2;
        audios_osc[i].volume = vol
        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `setting gabor/${i}.mp3 volume to ${vol}...`
        log.prepend(el)
    }

    volumes_timeout = setTimeout(setVolumes, 1000)
}

let startOscillation = () => {
    log = document.getElementById('log-osc')
    audios_osc = document.getElementsByClassName("oscillation")
    for (let i = 0; i < audios_osc.length; i++) {
        audios_osc[i].src = `https://static.enframed.net/poglos/gabor/${i}.mp3`
        audios_osc[i].onloadedmetadata = () => {
            audios_osc[i].play()
        }
    }

    setVolumes()
}

let startRandomDelayed = () => {
    audio_rd = document.getElementById('random-delayed')
    log = document.getElementById('log-rd')
    playRandomDelayed()
}

let playRandomDelayed = () => {
    index_rd = Math.floor(Math.random() * 6)
    audio_rd.src = `https://static.enframed.net/poglos/vexations/${index_rd}.mp3`
    audio_rd.onloadedmetadata = () => {
        audio_rd.play()

        let offset = audio_rd.duration * 1000 + Math.random() * silence_max + silence_min

        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `playing ${index_rd}, waiting ${Math.floor(offset / 1000)} seconds before next play...`
        log.prepend(el)
        if (timeout_rd) clearInterval(timeout_rd)
        timeout_rd = setTimeout(playRandomDelayed, offset)
    }
}

let startPolyphonic = () => {
    audios_pp = document.getElementsByClassName('polyphonic')
    log = document.getElementById('log-pp')
    for (let i = 0; i < audios_pp.length; i++) {
        playPolyphonic(i)
    }
}

let playPolyphonic = (i) => {    
        audios_pp[i].src = `https://static.enframed.net/poglos/swirl/${samples_pp[i]}/${Math.floor(Math.random() * samples_max_pp[i])}.mp3`
        audios_pp[i].onloadedmetadata = () => {
            audios_pp[i].play()

            let offset = audios_pp[i].duration * 1000 + Math.random() * silence_max + silence_min

            let el = document.createElement('div')
            el.setAttribute('class', 'msg')
            el.innerText += `playing ${samples_pp[i]}/${Math.floor(Math.random() * samples_max_pp[i])}.mp3`
            log.prepend(el)

            if (timeouts_pp[i]) clearInterval(timeouts_pp[i])
            timeouts_pp[i] = setTimeout(() => {playPolyphonic(i)}, offset)
        }
    
}