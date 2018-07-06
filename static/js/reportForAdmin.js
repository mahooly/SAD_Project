var fields = {
  "data": ["پیشنهاد همکاری", "امتیازدهی", "کمک مالی", "تغییر اطلاعات حساب کاربری"]
}
var sel = document.getElementById("field");
var opt = document.createElement('option');
opt.setAttribute('value', "blank")
opt.innerText = "زمینه فعالیت";
sel.appendChild(opt);
for (var i = 0; i < fields.data.length; i++) {
  var opt = document.createElement('option');
  opt.setAttribute('value',fields.data[i])
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

var params = ["فعالیت اعضا", "مسءولیت پذیری", "صداقت", "تعهد", "جو"]
var hours = ["۸-۱۰", "۱۰-۱۲", "۱۲-۱۵", "۱۵-۱۷"]
var days = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
var projects = {
  "projs": [
    {"id":1,"benefactor": "پژمان علی‌مرادی", "organization": "جمعیت امام علی", "ttype": "امتیازدهی", 
    "disc": "خیلی کادر خوبی دارن و خیلی تجربه خوبی بود", "rate": [3,4,2,3,5], "first": 1, "date": "1397/4/22-14:22"},
    {"id":2,"benefactor": "پویان شیرزادیان", "organization": "جمعیت امام علی", "ttype": "پیشنهاد همکاری", 
    "disc": "من میخوام بیام باهاتون کار کنم","week": [1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1], "first": 1, "date": "1397/4/22-13:12"},
    {"id":3,"benefactor": "پویان شیرزادیان", "organization": "یاوران ایتام", "ttype": "پیشنهاد همکاری", 
    "disc": "بیاین با ما کار کنین", "week": [1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,1,0,1,0,1,1], "first": 2, "date": "1397/4/18-04:17"},
    {"id":4,"benefactor": "مهراد حسن زاده", "organization": "صلیب سرخ", "ttype": "کمک مالی", 
    "disc": "پروژه خرید لباس برای کودکان", "payment" : 12000,"first": 1, "date": "1397/4/12-15:52"},
	{"id":5,"benefactor": "مهراد حسن زاده", "organization": "", "ttype": "تغییر اطلاعات حساب کاربری", 
    "disc": ["نام مستعار", "برنامه هفتگی", "توانایی‌ها"], "first": 3, "date": "1397/4/11-12:52"},
	{"id":6,"benefactor": "", "organization": "حلال احمر", "ttype": "تغییر اطلاعات حساب کاربری", 
    "disc": ["نیازمندی‌ها"], "first": 4, "date": "1397/4/۸-12:30"},
  ]
}

function show() {
var orgname = document.getElementById("orgName").value;
var projectfield = document.getElementById("field").value;
var beneName = document.getElementById("beneName").value;
  var divv = document.getElementById("result");
  while(divv.hasChildNodes()){
    divv.removeChild(divv.childNodes[0])
  }
  for (var i = 0; i < projects.projs.length; i++) {
    if ((orgname=='' || orgname==projects.projs[i].organization)
      &&(projectfield=="blank" ||projects.projs[i].ttype==projectfield)
      &&(beneName=='' ||projects.projs[i].benefactor>=beneName)){
      var rep = document.createElement('div');
      rep.setAttribute('class', "report");
	  rep.setAttribute('id', projects.projs[i].id);
      var peop = document.createElement('div');
      peop.setAttribute('class', "people");
      var benef = document.createElement('span');
      benef.setAttribute('class', "benefactor");
      benef.innerText = projects.projs[i].benefactor + "(نیکوکار)";
      var org = document.createElement('span');
      org.setAttribute('class', "organization");
      org.innerText = projects.projs[i].organization + "(موسسه)";
      var typ = document.createElement('span');
      typ.setAttribute('class', "type");
      typ.innerText = projects.projs[i].ttype;
	  var dat = document.createElement('span');
      dat.setAttribute('class', "type");
      dat.innerText = projects.projs[i].date;
      if (projects.projs[i].first==1) {
        peop.appendChild(benef);
        peop.appendChild(org);
      } if (projects.projs[i].first==2) {
        peop.appendChild(org);
        peop.appendChild(benef);
      } if (projects.projs[i].first==3) {
        peop.appendChild(benef);
      } if (projects.projs[i].first==4) {
        peop.appendChild(org);
      }
      peop.appendChild(typ);
	  peop.appendChild(dat);
      rep.appendChild(peop);
      if(projects.projs[i].ttype=="امتیازدهی") {
          var rating = document.createElement('div');
          rating.setAttribute('class', "rating");
          var ratingtable = document.createElement('table');
          for (var k = 0; k < 5; k++) {
            var ttr = document.createElement('tr');
            var ttd = document.createElement('td');
            ttd.setAttribute('class', "firstTd");
            ttd.innerText = params[k];
            ttr.appendChild(ttd);
            for (var j = 0; j < projects.projs[i].rate[k]; j++) {
                var ttd = document.createElement('td');
                var bbutton = document.createElement('button');
                ttd.appendChild(bbutton);
                ttr.appendChild(ttd);
            }
            ratingtable.appendChild(ttr);
          }
          rating.appendChild(ratingtable);
          rep.appendChild(rating);
          var more = document.createElement('div');
          more.setAttribute('class', "more");
          var hh3 = document.createElement('h3');
          hh3.innerHTML = projects.projs[i].disc;
          more.appendChild(hh3);
          var bbutton = document.createElement('button');
          bbutton.setAttribute('class', "remove");
          bbutton.setAttribute('onclick', "remove("+projects.projs[i].id+")");
          bbutton.innerText = "حذف";
          rep.appendChild(more);
          rep.appendChild(bbutton);
          divv.appendChild(rep);
      }   
      else if (projects.projs[i].ttype=="پیشنهاد همکاری" && projects.projs[i].first==1) {
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
            if (projects.projs[i].week[4*j+k]==1) {
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
        rep.appendChild(wweek);

        var mmore = document.createElement('div');
        mmore.setAttribute('class', "more");
        var hh3 = document.createElement('h3');
        hh3.innerHTML = projects.projs[i].disc;
        mmore.appendChild(hh3);
        rep.appendChild(mmore);
        divv.appendChild(rep);
      }
      else if (projects.projs[i].ttype=="پیشنهاد همکاری" && projects.projs[i].first==2) {
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
            if (projects.projs[i].week[4*j+k]==1) {
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
        rep.appendChild(wweek);

        var more = document.createElement('div');
        more.setAttribute('class', "more");
        var hh3 = document.createElement('h3');
        hh3.innerHTML = projects.projs[i].disc;
        more.appendChild(hh3);
        rep.appendChild(more);
        divv.appendChild(rep);
      } else if (projects.projs[i].ttype=="تغییر اطلاعات حساب کاربری") {
        var mmore = document.createElement('div');
        mmore.setAttribute('class', "more");
        var ull = document.createElement('ul');
		ull.style.listStyle= "circle";
		for(j=0;j<projects.projs[i].disc.length;j++){
			var lli = document.createElement('li');
			lli.style.fontSize = "15px";
			lli.innerHTML = projects.projs[i].disc[j];
			ull.appendChild(lli);
		}
        mmore.appendChild(ull);
        rep.appendChild(mmore);
        divv.appendChild(rep);
      }
      else {
        var ddiv = document.createElement('div');
        ddiv.setAttribute('class', "proj");
        var hh3 = document.createElement('h3');
        hh3.innerHTML = "مبلغ: " + projects.projs[i].payment;
        ddiv.appendChild(hh3);
        rep.appendChild(ddiv);

        var more = document.createElement('div');
        more.setAttribute('class', "more");
        var hh3 = document.createElement('h3');
        hh3.innerHTML = projects.projs[i].disc;
        more.appendChild(hh3);
        rep.appendChild(more);
        divv.appendChild(rep);
      }
    }
  }
}

show();

function remove(id) {
	var formm = document.getElementById("formRemove");
	while(formm.hasChildNodes()){
		formm.removeChild(formm.childNodes[0])
	}
	var button1 = document.createElement('button');
	button1.setAttribute('class', "exit");
	button1.setAttribute('onclick', "popdownregister()");
	var txt = document.createTextNode("\u00D7");
	button1.appendChild(txt);
	button1.setAttribute('id', "button"+id);
	formm.appendChild(button1);
	var p1 = document.createElement('p');
	p1.setAttribute('class',"title");
	p1.innerText = "امتیاز داده شده از لیست امتیازات حذف شود؟";
	formm.appendChild(p1);
	var div1 = document.createElement('div');
	div1.setAttribute('class', "enter");
	var button1 = document.createElement('button');
	button1.setAttribute('class', "yes");
	button1.setAttribute('id', "buttonyes"+id);
	button1.setAttribute('onclick', "removeFromList("+id+")");
	button1.innerText = "بله";
	div1.appendChild(button1);
	formm.appendChild(div1);
	var div1 = document.createElement('div');
	div1.setAttribute('class', "enter");
	var button1 = document.createElement('button');
	button1.setAttribute('onclick', "popdownregister()");
	button1.setAttribute('id', "buttonno"+id);
	button1.innerText = "خیر";
	div1.appendChild(button1);
	formm.appendChild(div1);
	document.getElementById("testreg").style.display = "block";
	f("buttonno"+id);
	f("buttonyes"+id);
	f("button"+id);
}
function popdownregister(id) {
	document.getElementById("testreg").style.display = "none";
}
function removeFromList(id) {
	document.getElementById(id).style.display = "none";
	document.getElementById("testreg").style.display = "none";
}
function f(id) {
    document.getElementById(id).addEventListener("click", function(event){
        event.preventDefault()
    });
}
