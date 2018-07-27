var buttons = document.getElementsByClassName("exit");
for (var i = 0 ; i < buttons.length; i ++) {
    buttons[i].addEventListener("click", function(event){
		event.preventDefault()
	});
}

buttons = document.getElementsByTagName("button");
for (var i = 0 ; i < buttons.length; i ++) {
    buttons[i].addEventListener("click", function(event){
		event.preventDefault()
	});
}


function popupProject(e) {
    document.getElementById(e).style.display = "block";
}

function popdownProject(e) {
    document.getElementById(e).style.display = "none";
}

var ull = document.getElementById("reqIds");
var lis = [];
while (ull.hasChildNodes()) {
	lis.unshift(ull.childNodes[0].value);
	ull.removeChild(ull.childNodes[0]);
}

for (var k = 0; k < lis.length; k++) {
    for (i = 1; i <= 7; i++) {
        var j;
        for (j = 1; j <= 4; j++) {
            if (document.getElementById('a' + lis[k] + 'b' + ((i - 1) * 4 + j - 1)).checked === true) {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(150,150,150)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 3;
            } else {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(211,233,158)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 2;
            }
        }
    }
}

function week(a,e,t) {
    if (document.getElementById('a'+a+'a'+e).value === 1) {
        document.getElementById('a'+a+'a'+e).style.backgroundColor = "rgb(211,233,158)";
        document.getElementById('a'+a+'c'+t).checked = false;
        document.getElementById('a'+a+'a'+e).value = 2;
    } else if (document.getElementById('a'+a+'a'+e).value === 2) {
        document.getElementById('a'+a+'a'+e).style.backgroundColor = "rgb(57,183,250)";
        document.getElementById('a'+a+'a'+e).value = 1;
        document.getElementById('a'+a+'c'+t).checked = true;
    }
}