var app = new Vue({
    el: '#app',
    data: {
        host: "localhost:2046",
        status: "Nothing is currently playing.",
        volume: 0,
        compositions: [],
        current: null
    },
    methods: {
        start: function (_name) {
            console.log(`requesting play ${_name}`);
            fetch(`http://${this.host}/start?composition=${_name}`)
                .then(res => {
                    return res.json()
                })
                .then((_composition) => {
                    this.current = _composition
                })
        },
        stop: function () {
            fetch(`http://${this.host}/stop`)
                .then(res => {
                    this.current = null
                })
        },
        setVolume: function (_evt) {
            this.volume = _evt.target.value;
            
            fetch(`http://${this.host}/volume?vol=${this.volume}`)
                .then(res => {
                    console.log(res.status);
                })
        },
        fetchState: function() {
            fetch(`http://${this.host}/state`)
            .then(res => {
                if(res.status == 200)
                    return res.json()
                else
                    setTimeout(fetchState, 1000)
                    return null
                
            }).then(data => {
                this.compositions = data.compositions
                this.current = data.current

                this.volume = data.preferences.volume * 100
                document.getElementById("volume").innerText = this.volume
                document.getElementById("volume-slider").value = this.volume
                
                console.log(`fetched compositions: ${JSON.stringify(this.compositions)}`);
                console.log(`fetched current: ${JSON.stringify(this.current)}`);
            })
        }
    },
    mounted: function () {
        console.log("pogłos v1.0");
        this.fetchState()
    }
})