let log, player, performer

let index = 0

let _notes = [
    "a.wav",
    // "b.wav",
    // "c.wav",
    // "d.wav",
    // "e.wav",
    "f.wav",
    "g.wav"
]

let rhodes = [
    // "61821-a-0.wav",
    // "61822-a0.wav",
    // "61823-b0.wav",
    // "61824-c-1.wav",
    // "61825-c1.wav",
    // "61826-d-1.wav",
    // "61827-d1.wav",
    // "61828-e0.wav",
    // "61829-f-0.wav",
    // "61830-f0.wav",
    // "61831-g-0.wav",
    // "61832-g0.wav",
    // "65650-a-5.wav",
    "65651-a5.wav",
    // "65652-b5.wav",
    // "65653-c-6.wav",
    // "65654-c6.wav",
    // "65655-d-5.wav",
    // "65656-d-6.wav",
    "65657-d5.wav",
    // "65658-d6.wav",
    // "65659-e5.wav",
    // "65660-e6.wav",
    // "65661-f-5.wav",
    "65662-f5.wav",
    // "65663-g-5.wav",
    // "65664-g5.wav",

    // "65714-a-2.wav",
    // "65715-a2.wav",
    // "65716-b2.wav",
    // "65717-c-2.wav",
    // "65718-c-3.wav",
    // "65719-c2.wav",
    // "65720-c3.wav",
    // "65721-d-2.wav",
    // "65722-d-3.wav",
    // "65723-d2.wav",
    "65724-d3.wav",
    // "65725-e2.wav",
    // "65726-e3aif.wav",
    // "65727-f-2.wav",
    // "65728-f2.wav",
    // "65729-g-2.wav",
    // "65730-g2.wav",
    // "65754-a-2.wav",
    // "65755-a2.wav",
    // "65756-b2.wav",
    // "65757-d-1.wav",
    // "65758-e1.wav",
    // "65759-f-1.wav",
    // "65760-f1.wav",
    // "65761-g-1.wav",
    // "65762-g1.wav",
]

let start = () => {
    log = document.getElementById('log')
    audio = document.getElementById('audio')
    audio.volume = 0.1
    playNote()
}

let stop = () => {
    clearTimeout(performer)
}

let playNote = () => {
    index = Math.floor(Math.random()*rhodes.length)

    audio.src = `assets/rhodes/${rhodes[index]}`
    audio.volume = Math.random() * 0.1 + 0.1
    log.innerText = `playing ${rhodes[index]}`
    audio.play()
    

    if(Math.random() < 0.2)
        performer = setTimeout(playNote, Math.floor(Math.random()*6000)+3000)
    else
        performer = setTimeout(playNote, Math.floor(Math.random()*1000)+2000)
}