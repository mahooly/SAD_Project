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
    if (edu.value == "blank" || edu.value == "nothing") {
        document.getElementById("fieldOfEducation").style.display = "none";
    } else {
        document.getElementById("fieldOfEducation").style.display = "block";
    }
}

function participation() {
    var edu = document.getElementById("typeOfParticipation");
    if (edu.value == "atHome" || edu.value == "blank") {
        document.getElementById("tab").style.display = "none";
        document.getElementById("tab2").style.display = "none";
    } else {
        document.getElementById("tab").style.display = "block";
        document.getElementById("tab2").style.display = "block";
    }
}

function week(e,t) {
    if (document.getElementById(e).value === 1) {
        document.getElementById(e).style.backgroundColor = "rgb(211,233,158)";
        document.getElementById('a'+t).checked = false;
        document.getElementById(e).value = 2;
    } else {
        document.getElementById(e).style.backgroundColor = "rgb(57,183,250)";
        document.getElementById(e).value = 1;
        document.getElementById('a'+t).checked = true;
    }
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


