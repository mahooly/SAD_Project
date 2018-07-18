var fields = {
  "data": ["کودکان", "سالمندان ", "زنان سرپرست خانوار", "بیماران", "آموزش", "غیره"]
}
var sel = document.getElementById("field");
var opt = document.createElement('option');
opt.setAttribute('value', "blank")
opt.innerText = "زمینه فعالیت";
sel.appendChild(opt);
for (var i = 0; i < fields.data.length; i++) {
  var opt = document.createElement('option');
  opt.setAttribute('value', i)
  opt.innerText = fields.data[i];
  sel.appendChild(opt);
}

function rate (e1,e2) {
  var id1 = "button" + e1;
  for (var i = 1; i <= e2; i++) {
    document.getElementById(id1+i).style.backgroundColor = "#E0B0FF";
  }
  for (var i = e2+1; i < 6; i++) {
    document.getElementById(id1+i).style.background = "none";
  }
}

var projects = {}

function show() {
var orgname = document.getElementById("orgName").value;
var sortType = document.getElementById("sortType").value;
var projectfield = document.getElementById("field").value;
var minimumBudget = document.getElementById("minimumbudget").value;
var minimumtotalrating = document.getElementById("minimumtotalrating").value;
  var divv = document.getElementById("result");
  // while(divv.hasChildNodes()){
  //   divv.removeChild(divv.childNodes[0])
  // }
  for (var i = 0; i < projects.data.length; i++) {
	  var check = 1;
	  for(j=0; j<projects.data[i].type.length; j++)
		  if(projects.data[i].type[j]==projectfield)
			  check = 2;
    if ((orgname=='' || orgname==projects.data[i].name)
      &&(projectfield=="blank" ||check == 2)
      &&(minimumBudget=='' ||projects.data[i].cost>=minimumBudget)
      &&(minimumtotalrating=='' ||projects.data[i].rate>=minimumtotalrating)){
    var divProject = document.createElement('div');
    divProject.setAttribute('class', "project");
    var divspec = document.createElement('div');
    divspec.setAttribute('class', "specifications");
    var aname = document.createElement('a');
    aname.setAttribute('href', "#");
    aname.innerText = projects.data[i].name;
    divspec.appendChild(aname);
    var h3disc = document.createElement('h3');
    h3disc.innerHTML = projects.data[i].disc;
    divspec.appendChild(h3disc);
	var ull = document.createElement('ul');
	for(j=0; j<projects.data[i].type.length; j++){
		var lli = document.createElement('li');
		lli.innerText = fields.data[projects.data[i].type[j]];
		ull.appendChild(lli);
	}
	divspec.appendChild(ull);
    divProject.appendChild(divspec);


    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var value1 = document.createElement('input');
    value1.setAttribute('type', "number");
    value1.setAttribute('placeholder', "مبلغ مورد نظر");
    value1.setAttribute('id', "value1");
    divcost.appendChild(value1);
    var h3disc = document.createElement('a');
    h3disc.style.textDecoration = "none";
    h3disc.style.backgroundColor = "rgb(61, 177, 58)";
    h3disc.style.width = "60px";
    h3disc.style.fontSize = "12px";
    h3disc.style.display = "inline-block";
    h3disc.style.color = "#eeeeee";
    h3disc.style.borderRadius = "5px";
    h3disc.innerHTML = "پرداخت";
    h3disc.setAttribute('href', "bank.html");
    divcost.appendChild(h3disc);
    divProject.appendChild(divcost);

    var divcost = document.createElement('div');
    divcost.setAttribute('class', "cost");
    var h3disc = document.createElement('h3');
    h3disc.innerHTML = "مبلغ مورد نیاز";
    divcost.appendChild(h3disc);
    var spancost = document.createElement('span');
    spancost.setAttribute('class', "budget");
    spancost.innerHTML = projects.data[i].cost + "تومان";
    divcost.appendChild(spancost);
    divProject.appendChild(divcost);
    divv.appendChild(divProject);
  }
  }
}

show();
