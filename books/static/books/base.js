// time displayed on the page

function showTime(){
    var d = new Date();
    var hour = d.getHours();
    var min = d.getMinutes();
    var sec = d.getSeconds();
    var newHour;
    var newMin;
    var newSec;

    // changing hour
    if(hour.toString().length == 1){
        var newHour = "0" + hour;
    }else{
        var newHour = hour;
    }

    // changing minutes
    if(min.toString().length == 1){
        var newMin = "0" + min;
    }else{
        var newMin = min;
    }

    // changing seconds
    if(sec.toString().length == 1){
        var newSec = "0" + sec;
    }else{
        var newSec = sec;
    }

    // time to be displayed
    var displayTime = newHour + ":" + newMin + ":" + newSec;

    // write on page
    document.getElementById("time").innerHTML = displayTime;
}

// runs this function every one second in order to display seconds
setInterval(showTime, 1000);