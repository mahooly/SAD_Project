function addItem(){
    var ul = document.getElementById("dynamiclist");
    var candidate = document.getElementById("candidate").value;
    var li = document.createElement("li");
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    span.appendChild(txt);
    li.appendChild(span);
    li.setAttribute('id',candidate);
    li.appendChild(document.createTextNode(candidate));
    ul.appendChild(li);
    
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
} 
f();

var cities = ["تهران","مشهد","اصفهان","شیراز"]
var sel = document.getElementById('city');
for (i=0;i<cities.length;i++) {
	var opt = document.createElement('option');
	opt.setAttribute('value', cities[i]);
	opt.innerHTML = cities[i];
	sel.appendChild(opt);
}

var abilities = ["رانندگی","روابط عمومی","حسابداری","آموزش"]
var sel = document.getElementById('candidate');
for (i=0;i<abilities.length;i++) {
	var opt = document.createElement('option');
	opt.setAttribute('value', abilities[i]);
	opt.innerHTML = abilities[i];
	sel.appendChild(opt);
}

var personalData ={
    "name": "یاوران ایتام",
    "parvaneh": "۱۲۲۴۱-۲۳",
    "date": 25,
    "month": 2,
    "Year": 1374,
    "nationalId": 1234123456,
    "city": "تهران",
    "addr": "خیابان آزادی، دانشگاه صنعتی شریف",
    "email": "info@aytam.com",
    "tel": 2132568698,
    "site": "aytam.com",
    "abilities": ["آموزش", "روابط عمومی"],
    "more": "",
    "photo": "images/1.png",
    "openAtFriday": false,
    "openAtThursday": true
}
document.getElementById("name").value = personalData.name;
document.getElementById("web").value = personalData.site;
document.getElementById("parvaneh").value = personalData.parvaneh;
document.getElementById("date").value = personalData.date;
document.getElementById("month").value = personalData.month;
document.getElementById("year").value = personalData.Year;
document.getElementById("city").value = personalData.city;
document.getElementById("addr").value = personalData.addr;
document.getElementById("email").value = personalData.email;
document.getElementById("tel").value = personalData.tel;
document.getElementById("cm").value = personalData.more;
document.getElementById("checkboxfriday").checked = personalData.openAtFriday;
document.getElementById("checkboxthursday").checked = personalData.openAtThursday;
var ul = document.getElementById("dynamiclist");
for(i=0;i<personalData.abilities.length;i++) {
    var li = document.createElement("li");
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    span.onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
    li.appendChild(span);
    li.setAttribute('id',personalData.abilities[i]);
    li.appendChild(document.createTextNode(personalData.abilities[i]));
    ul.appendChild(li);
}