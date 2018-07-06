var fields = {
  "data": ["خیاطی", "حسابداری", "مدیریت", "نقاشی", "رانندگی", "آشپزی"]
}
var sel = document.getElementById("field");
var opt = document.createElement('option');
opt.setAttribute('value', "blank")
opt.innerText = "زمینه فعالیت";
sel.appendChild(opt);
for (var i = 0; i < fields.data.length; i++) {
  var opt = document.createElement('option');
  opt.setAttribute('value', fields.data[i])
  opt.innerText = fields.data[i];
  sel.appendChild(opt);
}
var ratings = [0,0,0,0,0];
function rate (e1,e2) {
  var id1 = "button" + e1;
  for (var i = 1; i <= e2; i++) {
    document.getElementById(id1+i).style.backgroundColor = "#E0B0FF";
  }
  for (var i = e2+1; i < 6; i++) {
    document.getElementById(id1+i).style.background = "none";
  }
  ratings[e1-1] = e2;
  show();
}

var abilities = {
  "benefactors": [
    {"name": "علی حسینی", "abilities": ["خیاطی", "حسابداری"], "age": 30,"rate":3, "ratings":[2.5,4.3,1.4,2.4,4]},
    {"name": "بهراد گل", "abilities": ["نقاشی", "خطاطی", "مدیریت"], "age": 20,"rate":3.5, "ratings":[3.5,3.3,2.6,3,2.3]},
    {"name": "آرش پوردامغانی", "abilities": ["رانندگی", "حسابداری"], "age": 25,"rate":2, "ratings":[5,1.3,1.2,4.1,2]},
    {"name": "سعید آقایی", "abilities": ["آشپزی", "خیاطی", "نقاشی","مدیریت", "حسابداری", "رانندگی"], "age": 40,"rate":4, "ratings":[2.5,4.3,1.4,2.4,4]}
  ]
}

function show() {
var orgname = document.getElementById("orgName").value;
var sortType = document.getElementById("sortType").value;
var projectfield = document.getElementById("field").value;
var minimumage = document.getElementById("minimumage").value;
var minimumtotalrating = document.getElementById("minimumtotalrating").value;
  var divv = document.getElementById("result");
  while(divv.hasChildNodes()){
    divv.removeChild(divv.childNodes[0])
  }
  for (var i = 0; i < abilities.benefactors.length; i++) {
    var check = 1;
    if (projectfield == "blank") check = 2;
    else {
      for (var j = 0; j < abilities.benefactors[i].abilities.length; j++) {
        if (abilities.benefactors[i].abilities[j]==projectfield)
          check=check+1;
      }
    }
    for (var j = 0; j < 5; j++) {
      if (ratings[j] <= abilities.benefactors[i].ratings[j])
        check = check+1;
    }
    if ((orgname=='' || orgname==abilities.benefactors[i].name)
      &&(check == 7)
      &&(minimumage=='' ||abilities.benefactors[i].age>=minimumage)
      &&(minimumtotalrating=='' ||abilities.benefactors[i].rate>=minimumtotalrating)){
    var divProject = document.createElement('div');
    divProject.setAttribute('class', "project");
    var divspec = document.createElement('div');
    divspec.setAttribute('class', "specifications");
    var aname = document.createElement('a');
    aname.setAttribute('href', "#");
    aname.innerText = abilities.benefactors[i].name;
    divspec.appendChild(aname);
    var ull = document.createElement('ul');
    for (var j = 0; j < abilities.benefactors[i].abilities.length; j++) {
      lli = document.createElement('li');
      lli.innerText = abilities.benefactors[i].abilities[j];
      ull.appendChild(lli);
    }
    divspec.appendChild(ull);
    divProject.appendChild(divspec);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var h3disc = document.createElement('h3');
    h3disc.innerHTML = "سن";
    divcost.appendChild(h3disc);
    var spancost = document.createElement('span');
    spancost.setAttribute('class', "budget");
    spancost.innerHTML = abilities.benefactors[i].age;
    divcost.appendChild(spancost);
    divProject.appendChild(divcost);
    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var h3rate = document.createElement('h3');
    h3rate.innerHTML = "میانگین امتیاز";
    divcost.appendChild(h3rate);
    var spancost = document.createElement('span');
    spancost.setAttribute('class', "budget");
    spancost.innerHTML = abilities.benefactors[i].rate;
    divcost.appendChild(spancost);
    divProject.appendChild(divcost);
    divv.appendChild(divProject);
  }
  }
}

show();
