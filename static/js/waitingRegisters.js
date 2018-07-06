var users = {
  "benefactors": [
    {"name": "علی حسینی", "nickname": "حصین"},
    {"name": "بهراد گل", "nickname": "بهگل"},
    {"name": "حمید هاشمی", "nickname": "حمهاش"},
    {"name": "سینا سعیدنیا", "nickname": "سینا"}
  ],
  "organizations": [
    {"name": "بنیاد خیریه احسان"},
    {"name": "جمعیت امام علی"},
    {"name": "یاوران ایتام"}
  ]
}

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
    divProject.appendChild(divspec);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var button1 = document.createElement('button');
    button1.innerText = "رد";
    button1.style.backgroundColor = "rgb(188, 0, 58)";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "reject("+i+",1)");
    divcost.appendChild(button1);
    divProject.appendChild(divcost);
    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var button1 = document.createElement('button');
    button1.innerText = "تایید";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "accept("+i+",1)");
    button1.style.backgroundColor = "rgb(61, 177, 58)";
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
    aname.setAttribute('href', "personalProfileOrganization.html");
    aname.innerText = users.organizations[i].name;
    divspec.appendChild(aname);
    divProject.appendChild(divspec);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var button1 = document.createElement('button');
    button1.innerText = "رد";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "reject("+i+",2)");
    button1.style.backgroundColor = "rgb(188, 0, 58)";
    divcost.appendChild(button1);
    divProject.appendChild(divcost);
    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var button1 = document.createElement('button');
    button1.innerText = "تایید";
    button1.addEventListener("click", function(event){
        event.preventDefault()
    });
    button1.setAttribute('onclick', "accept("+i+",2)");
    button1.style.backgroundColor = "rgb(61, 177, 58)";
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