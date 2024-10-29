const socket = new WebSocket('ws://localhost:8000/ws/plc/');

socket.onopen = function(e) {
    console.log("WebSocket connection established.");
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    if (data.status === 'success') {
        console.log("Input Values:", data.input_values);
        console.log("Output Values:", data.output_values);
        document.getElementById("input-values").innerHTML = data.input_values.join(", ");
        document.getElementById("output-values").innerHTML = data.output_values.join(", ");
    } else {
        console.log("Error:", data.message);
    }
};

socket.onclose = function(e) {
    console.log("WebSocket connection closed.");
};
