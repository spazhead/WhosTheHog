var socket = io();
var progress = 0.0;
var progressInterval;

var drawStatus = function(status) {
	switch (status) {
   		case "collecting":
   		case "calculating":
   			$(".status").text("Collecting data... "+(progress*100).toFixed(2)+"%")
   			break;
   		case "done":
            $(".status").text("Getting results...")
            socket.emit()
   			break;
   		case "error":
			$(".status").addClass("error").text("Error occured! Check server logs for details.")
   			break;
   		default:
   			$(".status").text("Unknown status "+status);
   	}
}

socket.on('status', function(status) {
   	console.log("new status ", data);
   	drawStatus(status);
});

socket.on('progress', function(data) {
   	progress = data;
   	console.log("new progress ", data);
   	drawStatus();
});

socket.on('result', function(data) {

})