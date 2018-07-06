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
    document.getElementById("education").addEventListener("change", function(event){
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

var week = {
    "day": ["شنبه", "یکشنبه", "دوشنبه" ,"سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"],
    "hour": [" ", "۸-۱۰", "۱۰-۱۲", "۱۲-۱۵", "۱۵-۱۷"]
}
var personalData ={
    "name": "علی",
    "lastname": "حسینی",
    "nickname": "حسین",
    "sex": "male",
    "birthdate": 25,
    "birthmonth": 2,
    "birthYear": 1374,
    "education": "master",
    "fieldOfEducation": "مهندسی کامپیوتر",
    "nationalId": 1234123456,
    "city": "تهران",
    "addr": "خیابان آزادی، دانشگاه صنعتی شریف",
    "email": "ahoseini@gmail.com",
    "tel": 9123256898,
    "abilities": ["آموزش", "روابط عمومی"],
    "typeOfParticipation": "inOffice20",
    "week": [1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0],
    "more": "",
    "photo": "images/1.png"
}
document.getElementById("name").value = personalData.name;
document.getElementById("lastname").value = personalData.lastname;
document.getElementById("nickname").value = personalData.nickname;
document.getElementById("sex").value = personalData.sex;
document.getElementById("date").value = personalData.birthdate;
document.getElementById("month").value = personalData.birthmonth;
document.getElementById("year").value = personalData.birthYear;
document.getElementById("education").value = personalData.education;
if (personalData.education!="blank" && personalData.education!="nothing") {
    document.getElementById("fieldOfEducation").style.display = "block";
    document.getElementById("fieldOfEducation").value = personalData.fieldOfEducation;
}
document.getElementById("nationalId").value = personalData.nationalId;
document.getElementById("city").value = personalData.city;
document.getElementById("addr").value = personalData.addr;
document.getElementById("email").value = personalData.email;
document.getElementById("tel").value = personalData.tel;
document.getElementById("typeOfParticipation").value = personalData.typeOfParticipation;
if (personalData.typeOfParticipation == "atHome" || personalData.typeOfParticipation == "blank") {
    document.getElementById("tab").style.display = "none";
} else {
    document.getElementById("tab").style.display = "block";
    var table = document.getElementById('tab');
    var thead = document.createElement('tr');
    for (var i = 0; i < week.hour.length; i++) {
        var th = document.createElement('td');
        th.innerText = week.hour[i];
        thead.appendChild(th);
    }
    table.appendChild(thead);
    for (var i = 0; i < 7; i++) {
        var row = document.createElement('tr');
        var data = document.createElement('td');
        data.innerText = week.day[i];
        row.appendChild(data);
        for (var j = 0; j < 4; j++) {
            var d = document.createElement('td');
            var span = document.createElement('span');
            var id = i*4+j;
            span.id = id;
            if (personalData.week[id] == 0) {
                span.style.backgroundColor = "rgb(191,215,157)";
                span.value = 0;
            }
            if (personalData.week[id] == 1) {
                span.style.backgroundColor = "rgb(150,150,150)";
                span.value = 1;
            }
            span.onclick = function() {
                    if (this.value == 1) {
                        this.style.backgroundColor = "rgb(191,215,157)";
                        this.value = 0;
                    }
                    else {
                        this.style.backgroundColor = "rgb(150,150,150)";
                        this.value = 1;
                    }
                };
            d.appendChild(span);
            row.appendChild(d);
        }
        table.appendChild(row);
    }
}
document.getElementById("cm").value = personalData.more;
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

var abilities = ["رانندگی","روابط عمومی","حسابداری","آموزش"]
var sel = document.getElementById('candidate');
for (i=0;i<abilities.length;i++) {
    var opt = document.createElement('option');
    opt.setAttribute('value', abilities[i]);
    opt.innerHTML = abilities[i];
    sel.appendChild(opt);
}
