var templist = document.getElementById("templist");
while (templist.hasChildNodes()) {
    add(templist.childNodes[0].id);
    templist.removeChild(templist.childNodes[0]);
}

function add(candidate1) {
    var ul = document.getElementById("dynamiclist");
    document.getElementById(candidate1).checked = true;
    var li2 = document.createElement("li");
    var span = document.createElement("SPAN");
    span.id = candidate1;
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
            document.getElementById(this.id).checked = false;
        };
    span.appendChild(txt);
    li2.appendChild(span);
    //li.setAttribute('id',candidate1);
    li2.appendChild(document.createTextNode(candidate1));
    ul.appendChild(li2);

    document.getElementById("candidate").value = "";
}

function addItem(){
    var ul = document.getElementById("dynamiclist");
    var candidate1 = document.getElementById("candidate").value;
    document.getElementById(candidate1).checked = true;
    var li2 = document.createElement("li");
    var span = document.createElement("SPAN");
    span.id = candidate1;
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
            document.getElementById(this.id).checked = false;
        };
    span.appendChild(txt);
    li2.appendChild(span);
    //li.setAttribute('id',candidate1);
    li2.appendChild(document.createTextNode(candidate1));
    ul.appendChild(li2);
    
    document.getElementById("candidate").value = "";
}

function eduChanged() {
    var edu = document.getElementById("education");
    if (edu.value === "blank" || edu.value === "nothing") {
        document.getElementById("fieldOfEducation").style.display = "none";
    } else {
        document.getElementById("fieldOfEducation").style.display = "block";
    }
}

function participation() {
    var edu = document.getElementById("typeOfParticipation");
    if ("atHome" === edu.value || edu.value === "blank") {
        document.getElementById("tab").style.display = "none";
    } else {
        document.getElementById("tab").style.display = "block";
    }
}

function week(e) {
    document.getElementById(e).style.backgroundColor = "rgb(57,183,250)";
}

function f() {
    document.getElementById("add").addEventListener("click", function(event){
        event.preventDefault()
    });
    document.getElementById("education").addEventListener("change", function(event){
        event.preventDefault()
    });
} 
f();
var cities = ["تهران","مشهد","اصفهان","شیراز"];
var sel = document.getElementById('city');
for (var i=0;i<cities.length;i++) {
    var opt = document.createElement('option');
    opt.setAttribute('value', cities[i]);
    opt.innerHTML = cities[i];
    sel.appendChild(opt);
}
