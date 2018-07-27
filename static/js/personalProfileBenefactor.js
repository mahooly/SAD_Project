for (i = 1; i <=7; i ++) {
    var j;
    for (j = 1; j <= 4; j ++ ) {
        if (document.getElementById('a' + ((i-1)*4+j-1)).checked === true) {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(150,150,150)";
            document.getElementById(i + "" + j).style.display = "inline-block";
            document.getElementById(i + "" + j).style.width = "100%";
            document.getElementById(i + "" + j).style.heigth = "30px";
        } else {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(211,233,158)";
            document.getElementById(i + "" + j).style.display = "inline-block";
            document.getElementById(i + "" + j).style.width = "100%";
            document.getElementById(i + "" + j).style.height = "30px";

        }
    }
}

function popupDelete() {
    document.getElementById("delete").style.display="block";
}

function popdownDelete() {
    document.getElementById("delete").style.display="none";
}

document.getElementById("not").addEventListener("click", function (e) {
    e.preventDefault()
});