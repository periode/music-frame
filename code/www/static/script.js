console.log("hello");

host = "localhost:2046"

let init = () => {
    fetch(`http://${host}/state`)
    .then(res => {
        console.log(res.status);
    })   
}

let start = () => {
    fetch(`http://${host}/start`)
    .then(res => {
        console.log(res.status);
    })
}

let stop = () => {
    fetch(`http://${host}/stop`)
    .then(res => {
        console.log(res.status);
    })
}