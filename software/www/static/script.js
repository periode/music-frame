var app = new Vue({
    el: '#app',
    data: {
        host: "archpierre:2046",
        socket: null,
        status: "Nothing is playing.",
        connected: false,
        volume: 0,
        compositions: [],
        current: null,
        showHelp: false,
        showVolume: false
    },
    methods: {
        start: function (_name) {
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
            if (_data.composition)
                this.current = _data.composition
            else
                console.error('No composition field on socket response!');
        })
    }
})