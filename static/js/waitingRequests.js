var users = {
  "organizations": [
    {"name": "علی حسینی", "nickname": "حصین", "abilities": ["امور مالی", "روابط عمومی"], "week" : [1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
    "more": "من خیلی علاقه‌مندم با شما کار کنم"},
    {"name": "بهراد گل", "nickname": "بهگل", "abilities": ["روابط عمومی"], "week" :  [1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,0,0,0],
    "more": ""},
    {"name": "حمید هاشمی", "nickname": "حمهاش", "abilities": ["روابط عمومی"], "week" :  [0,0,1,1,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
    "more": "من خیلی علاقه‌مندم با شما کار کنم"},
    {"name": "سینا سعیدنیا", "nickname": "سینا", "abilities": ["امور مالی", "روابط عمومی"],"week" :  [1,1,1,1,1,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0],
    "more": "مطمئن باشید ناامیدتان نخواهم کرد"}
  ],
  "benefactors": []
}

var hours = ["۸-۱۰", "۱۰-۱۲", "۱۲-۱۵", "۱۵-۱۷"]
var days = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]

function show() {
  var divv = document.getElementById("result");
  while(divv.hasChildNodes()){
    divv.removeChild(divv.childNodes[0])
  }
  for (var i = 0; i < users.benefactors.length; i++) {
    var divProject = document.createElement('div');
    divProject.setAttribute('class', "project");
    divProject.setAttribute('id', "id"+i+"1");
    var divspec = document.createElement('div');
    divspec.setAttribute('class', "specifications");
    var aname = document.createElement('a');
    aname.setAttribute('href', "personalProfileBenefactor.html");
    aname.innerText = users.benefactors[i].name + " ( "+ users.benefactors[i].nickname+ " ) ";
    divspec.appendChild(aname);
    var ull = document.createElement('ul');
    for (var j = 0; j < users.benefactors[i].abilities.length; j++) {
      lli = document.createElement('li');
      lli.innerText = users.benefactors[i].abilities[j];
      ull.appendChild(lli);
    }
    divspec.appendChild(ull);
    divProject.appendChild(divspec);

    var wweek = document.createElement('div');
    wweek.setAttribute('class', "week");
    var ttable = document.createElement('table');
    ttable.setAttribute('class', "tab");
    var tthead = document.createElement('thead');
    var tth = document.createElement('th');
    tth.setAttribute('class', "firstCol");
    tth.innerText = "";
    tthead.appendChild(tth);
    for (var j = 0; j < 4; j++) {
      var tth = document.createElement('th');
      tth.innerText = hours[j];
      tthead.appendChild(tth);
    }
    ttable.appendChild(tthead);
    var ttbody = document.createElement('tbody');
    for (var j = 0; j <7; j++) {
      var ttr = document.createElement('tr');
      var ttd = document.createElement('td');
      ttd.setAttribute('class', "firstCol");
      ttd.innerText = days[j];
      ttr.appendChild(ttd);
      for (var k = 0; k < 4; k++) {
        var ttd = document.createElement('td');
        ttd.setAttribute('class', "otherCol");
        ttd.innerText = "";
        if (users.benefactors[i].week[4*j+k]==1) {
          ttd.style.backgroundColor = "rgb(211,233,158)";
        } else {
          ttd.style.backgroundColor = "#999999";
        }
        ttr.appendChild(ttd);
      }
      ttbody.appendChild(ttr);
    }
    ttable.appendChild(ttbody);
    wweek.appendChild(ttable);
    divProject.appendChild(wweek);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var h3 = document.createElement('h3');
    h3.innerText = users.benefactors[i].more;
    divcost.appendChild(h3);
    var button1 = document.createElement('button');
    button1.innerText = "تایید";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "accept("+i+",1)");
    button1.style.backgroundColor = "rgb(61, 177, 58)";
    divcost.appendChild(button1);
    var button1 = document.createElement('button');
    button1.innerText = "رد";
    button1.style.backgroundColor = "rgb(188, 0, 58)";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "reject("+i+",1)");
    divcost.appendChild(button1);
    
    divProject.appendChild(divcost);
    divv.appendChild(divProject);
  }
  for (var i = 0; i < users.organizations.length; i++) {
    var divProject = document.createElement('div');
    divProject.setAttribute('class', "project");
    divProject.setAttribute('id', "id"+i+"2");
    var divspec = document.createElement('div');
    divspec.setAttribute('class', "specifications");
    var aname = document.createElement('a');
    aname.setAttribute('href', "personalProfileOrganizations.html");
    aname.innerText = users.organizations[i].name + " ( "+ users.organizations[i].nickname+ " ) ";
    divspec.appendChild(aname);
    var ull = document.createElement('ul');
    for (var j = 0; j < users.organizations[i].abilities.length; j++) {
      lli = document.createElement('li');
      lli.innerText = users.organizations[i].abilities[j];
      ull.appendChild(lli);
    }
    divspec.appendChild(ull);
    divProject.appendChild(divspec);

    var wweek = document.createElement('div');
    wweek.setAttribute('class', "week");
    var ttable = document.createElement('table');
    ttable.setAttribute('class', "tab");
    var tthead = document.createElement('thead');
    var tth = document.createElement('th');
    tth.setAttribute('class', "firstCol");
    tth.innerText = "";
    tthead.appendChild(tth);
    for (var j = 0; j < 4; j++) {
      var tth = document.createElement('th');
      tth.innerText = hours[j];
      tthead.appendChild(tth);
    }
    ttable.appendChild(tthead);
    var ttbody = document.createElement('tbody');
    for (var j = 0; j <7; j++) {
      var ttr = document.createElement('tr');
      var ttd = document.createElement('td');
      ttd.setAttribute('class', "firstCol");
      ttd.innerText = days[j];
      ttr.appendChild(ttd);
      for (var k = 0; k < 4; k++) {
        var ttd = document.createElement('td');
        ttd.setAttribute('class', "otherCol");
        ttd.innerText = "";
        if (users.organizations[i].week[4*j+k]==1) {
          ttd.style.backgroundColor = "rgb(211,233,158)";
        } else {
          ttd.style.backgroundColor = "#999999";
        }
        ttr.appendChild(ttd);
      }
      ttbody.appendChild(ttr);
    }
    ttable.appendChild(ttbody);
    wweek.appendChild(ttable);
    divProject.appendChild(wweek);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var h3 = document.createElement('h3');
    h3.innerText = users.organizations[i].more;
    divcost.appendChild(h3);
    var button1 = document.createElement('button');
    button1.innerText = "تایید";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "accept("+i+",2)");
    button1.style.backgroundColor = "rgb(61, 177, 58)";
    divcost.appendChild(button1);
    var button1 = document.createElement('button');
    button1.innerText = "رد";
    button1.style.backgroundColor = "rgb(188, 0, 58)";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "reject("+i+",2)");
    divcost.appendChild(button1);
    
    divProject.appendChild(divcost);
    divv.appendChild(divProject);
  }
}

show();

function accept (i1,i2) {
  document.getElementById("id"+i1+i2).style.display = "none";
}
function reject (i1,i2) {
  document.getElementById("id"+i1+i2).style.display = "none";
}
