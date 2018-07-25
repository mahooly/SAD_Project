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