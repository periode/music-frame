var app = new Vue({
    el: '#app',
    data: {
        host: `${window.location.origin}:2046`,
        socket: null,
        status: "nothing is playing.",
        connected: false,
        volume: 0,
        compositions: [],
        current: null,
        showHelp: false,
        showVolume: false,
        showCompositions: false
    },
    methods: {
        start: function (_name) {
            this.current = null
            this.status = `Requesting playback for ${_name}...`
            this.showCompositions = false
            this.socket.emit('start', _name)
        },
        stop: function () {
            this.socket.emit('stop')
        },
        setVolume: function (_evt) {
            this.volume = _evt.target.value;

            this.socket.emit('volume', this.volume)
        },
    },
    mounted: function () {
        console.log("pogłos v1.0");
        this.socket = io(this.host)

        this.socket.on('connect', (_data) => {
            this.connected = true
        })

        this.socket.on('disconnect', () => {
            this.connected = false
            this.current = null
        })

        this.socket.on("connect_error", () => {
            setTimeout(() => { this.socket.connect(); }, 1000);
        });

        this.socket.on('state', (_data) => {
            this.compositions = _data.compositions
            this.current = _data.current
            this.volume = _data.preferences.volume * 100

            console.log(`fetched compositions: ${JSON.stringify(this.compositions)}`);
            console.log(`fetched current: ${JSON.stringify(this.current)}`);
        })

        this.socket.on('status', (_data) => {
                this.current = _data.composition
                if(!this.current) this.status = "nothing is playing."
        })
    }
})