var buttons = document.getElementsByClassName("exit");
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

function popupDelete() {
    document.getElementById("delete").style.display="block";
}

function popdownDelete() {
    document.getElementById("delete").style.display="none";
}

function deleteReq(e) {
    document.getElementById("delete"+e).style.display="block";
}

function popdownDeleteReq(e) {
    document.getElementById("delete"+e).style.display="none";
}

document.getElementById("not").addEventListener("click", function (e) {
    e.preventDefault()
});

