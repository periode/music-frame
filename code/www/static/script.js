var app = new Vue({
    el: '#app',
    data: {
        host: "localhost:2046",
        status: "Nothing is currently playing.",
        volume: 0,
        compositions: []
    },
    methods: {
        start: function (_name) {
            console.log(`requesting play ${_name}`);
            fetch(`http://${this.host}/start?composition=${_name}`)
                .then(res => {
                    console.log(res.status);
                })
        },
        stop: function () {
            fetch(`http://${this.host}/stop`)
                .then(res => {
                    console.log(res.status);
                })
        },
        setVolume: function (_evt) {
            this.volume = _evt.target.value;
            
            fetch(`http://${this.host}/volume?vol=${this.volume}`)
                .then(res => {
                    console.log(res.status);
                })
        }
    },
    mounted: function () {
        console.log("pogłos v1.0");
        fetch(`http://${this.host}/state`)
            .then(res => {
                console.log(res.status);
                return res.json()
            }).then(data => {
                this.compositions = data
                console.log(`fetched compositions: ${JSON.stringify(this.compositions)}`);
            })
    }
})