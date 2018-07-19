var ab = document.getElementById("abilities1");
for (i = 0; i < ab.childNodes.length; i++) {
    ab.childNodes[i].onclick = function() {
        if (this.value === 1) {
            this.style.backgroundColor = "rgba(0,0,0,0.4)";
            this.value = 2;
            document.getElementById('d'+this.id).checked = false;
        }
        else {
            this.style.backgroundColor = "rgb(4,80,255)";
            this.value = 1;
            document.getElementById('d'+this.id).checked = true;
        }
    };
}

function week(e,t) {
    if (document.getElementById(e).value === 1) {
        document.getElementById(e).style.backgroundColor = "rgb(211,233,158)";
        document.getElementById('c'+t).checked = false;
        document.getElementById(e).value = 2;
    } else if (document.getElementById(e).value === 2) {
        document.getElementById(e).style.backgroundColor = "rgb(57,183,250)";
        document.getElementById(e).value = 1;
        document.getElementById('c'+t).checked = true;
    }
}

for (i = 1; i <=7; i ++) {
    var j;
    for (j = 1; j <= 4; j ++ ) {
        if (document.getElementById('a' + ((i-1)*4+j-1)).checked === true) {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(150,150,150)";
            document.getElementById(i + "" + j).value = 3;
        } else {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(211,233,158)";
            document.getElementById(i + "" + j).value = 2;
        }
    }
}