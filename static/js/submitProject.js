
document.getElementById("add").addEventListener("click", function(event){
    event.preventDefault()
});


function addItem(){
    var ul = document.getElementById("dynamiclist");
    var candidate1 = document.getElementById("candidate").value;
    document.getElementById('a'+candidate1).checked = true;
    var li2 = document.createElement("li");
    var span = document.createElement("SPAN");
    span.id = candidate1;
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
            document.getElementById('a'+this.id).checked = false;
        };
    span.appendChild(txt);
    li2.appendChild(span);
    //li.setAttribute('id',candidate1);
    li2.appendChild(document.createTextNode(candidate1));
    ul.appendChild(li2);

    document.getElementById("candidate").value = "";
}

function changed() {
	var way = document.getElementById("way").value;
	if (way==="blank") {
		document.getElementById("cardNum").style.display = "none";
		document.getElementById("accNum").style.display = "none";
	}
	if (way==="account") {
		document.getElementById("cardNum").style.display = "none";
		document.getElementById("accNum").style.display = "block";
	}
	if (way==="card") {
		document.getElementById("cardNum").style.display = "block";
		document.getElementById("accNum").style.display = "none";
	}
}