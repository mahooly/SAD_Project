var categories = ["کودکان کار","زنان سرپرست خانوار","سالمندان","آموزش", "ایتام"]
var sel =document.getElementById("candidate");
while(sel.hasChildNodes()) {
	sel.removeChild(sel.childNodes[0]);
}
var catProject = document.createElement('option');
catProject.setAttribute('value', "blank");
catProject.innerText="طبقه بندی";
sel.appendChild(catProject);
	for(var i=0;i<categories.length; i++){
		var catProject = document.createElement('option');
		catProject.setAttribute('value', categories[i]);
		catProject.innerText=categories[i];
		sel.appendChild(catProject);
	}
document.getElementById("add").addEventListener("click", function(event){
    event.preventDefault()
});
var close = document.getElementsByClassName("close");


function addItem(){
    var ul = document.getElementById("dynamiclist");
    var candidate = document.getElementById("candidate").value;
    var li = document.createElement("li");
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);
    li.setAttribute('id',candidate);
    li.appendChild(document.createTextNode(candidate));
    ul.appendChild(li);
    
    document.getElementById("candidate").value = "";

    for (i = 0; i < close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }
}

var cities = ["تهران","مشهد","اصفهان","شیراز"]
var sel = document.getElementById('city');
for (i=0;i<cities.length;i++) {
	var opt = document.createElement('option');
	opt.setAttribute('value', cities[i]);
	opt.innerHTML = cities[i];
	sel.appendChild(opt);
}

function changed() {
	var way = document.getElementById("way").value;
	if (way=="blank") {
		document.getElementById("cardNum").style.display = "none";
		document.getElementById("accNum").style.display = "none";
	}
	if (way=="account") {
		document.getElementById("cardNum").style.display = "none";
		document.getElementById("accNum").style.display = "block";
	}
	if (way=="card") {
		document.getElementById("cardNum").style.display = "block";
		document.getElementById("accNum").style.display = "none";
	}
}