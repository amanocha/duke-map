function printHeader(destination, message, speed){
    var i = 0;
    var interval = setInterval(function(){
        document.getElementById(destination).innerHTML += message.charAt(i);
        i++;
        if (i >= message.length){
            clearInterval(interval);
        }
    }, speed);
}

//printHeader("header1", "Duke\xa0MAP", 100);
//printHeader("header2", "Organizing\xa0research,\xa0promoting\xa0collaboration", 100);