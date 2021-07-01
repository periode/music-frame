let audio_rd, log_rd, timeout_rd
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

let toggleRandomDelayed = (_el) => {
    if(_el.innerText === 'play'){
        startRandomDelayed()
        _el.innerText = 'stop'
    }else if(_el.innerText === 'stop'){
        stopRandomDelayed()
        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `...stopping.`
        log_rd.prepend(el)
        _el.innerText = 'play'
    }
}

let startRandomDelayed = () => {
    audio_rd = document.getElementById('random-delayed')
    log_rd = document.getElementById('log-rd')
    playRandomDelayed()
}

let stopRandomDelayed = () => {
    if(audio_rd) audio_rd.pause()
    if(timeout_rd) clearTimeout(timeout_rd)
}

let playRandomDelayed = () => {
    index_rd = Math.floor(Math.random()*samples_rd.length)
    audio_rd.src = `assets/audio/${samples_rd[index_rd]}`
    audio_rd.onloadedmetadata = () => {
        audio_rd.play()

        let offset = audio_rd.duration * 1000 + Math.random()*silence_max + silence_min

        let el = document.createElement('div')
        el.setAttribute('class', 'msg')
        el.innerText += `playing ${samples_rd[index_rd]}, waiting ${Math.floor(offset/1000)} seconds before next play...`
        log_rd.prepend(el)
        if(timeout_rd) clearInterval(timeout_rd)
        timeout_rd = setTimeout(playRandomDelayed, offset)
    }
}