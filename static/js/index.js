function popup() {
    document.getElementById("test").style.display = "block";
    document.getElementById("testreg").style.display = "none";
}

function popdown() {
    document.getElementById("test").style.display = "none";
}
function popupregister() {
    document.getElementById("testreg").style.display = "block";
    document.getElementById("test").style.display = "none";
}

function popdownregister() {
    document.getElementById("testreg").style.display = "none";
}

function f(){
	document.getElementById("buttonreg").addEventListener("click", function(event){
		event.preventDefault()
	})
}
f();
var check = 0;
var p = document.getElementById('c1');
var ptop = 1;
var p2 = document.getElementById('c2');
var ptop2 = 1;
var p3 = document.getElementById('c3');
var ptop3 = 1;
var p4 = document.getElementById('c4');
var ptop4 = 1;
var p5 = document.getElementById('c5');
var ptop5 = 1;
window.addEventListener("scroll", function(){
	var scrollTop = window.pageYOffset || (document.documentElement || document.body.parentNode || document.body).scrollTop;
	if (scrollTop <= 920 && scrollTop >= 490 && (check == 0 || check == 2)){
		if (check == 0) {
			myLoop1();
		}
		else { 
			myLoop22();
		}
		check = 1;
	}
	if (scrollTop <= 920){
		myLoop22();
	}
	if (scrollTop <= 440){
		myLoop12();
		check = 0;
	}
	if (scrollTop <= 1400 && scrollTop >= 970 && (check == 1 || check == 3)){
		if (check == 1) {
			myLoop2();
		}
		else { 
			myLoop32();
		}
		check = 2;
	}
	if (scrollTop <= 1400){
		myLoop32();
	}
	if (scrollTop <= 1880 && scrollTop >= 1450 && (check == 2 || check == 4)){
		if (check == 2) {
			myLoop3();
		}
		else { 
			myLoop42();
		}
		check = 3;
	}
	if (scrollTop <= 1880){
		myLoop42();
	}
	if (scrollTop >= 1930 && check == 3 ){
		myLoop4();
		check = 4;
	}

}, false)

function myLoop1 () {          
   setTimeout(function () {   
   	  ptop = ptop-0.01;
      p.style.opacity = ptop;     
      if (ptop > 0.3) myLoop1(); 
   }, 50)
}
function myLoop12 () {          
   setTimeout(function () {
   	  if (ptop < 1){
   	  ptop = ptop+0.01;
      p.style.opacity = ptop;
      myLoop12(); }
   }, 50)
}
function myLoop2 () {          
   setTimeout(function () {   
   	  ptop2 = ptop2-0.01;
      p2.style.opacity = ptop2;     
      if (ptop2 > 0.3) myLoop2(); 
   }, 50)
}
function myLoop22 () {          
   setTimeout(function () {
   	  if (ptop2 < 1){
   	  ptop2 = ptop2+0.01;
      p2.style.opacity = ptop2;
      myLoop22(); }
   }, 50)
}
function myLoop3 () {          
   setTimeout(function () {   
   	  ptop3 = ptop3-0.01;
      p3.style.opacity = ptop3;     
      if (ptop3 > 0.3) myLoop3(); 
   }, 50)
}
function myLoop32 () {          
   setTimeout(function () {
   	  if (ptop3 < 1){
   	  ptop3 = ptop3+0.01;
      p3.style.opacity = ptop3;
      myLoop32(); }
   }, 50)
}
function myLoop4 () {          
   setTimeout(function () {   
   	  ptop4 = ptop4-0.01;
      p4.style.opacity = ptop4;     
      if (ptop4 > 0.3) myLoop4(); 
   }, 50)
}
function myLoop42 () {          
   setTimeout(function () {
   	  if (ptop4 < 1){
   	  ptop4 = ptop4+0.01;
      p4.style.opacity = ptop4;
      myLoop42(); }
   }, 50)
}

var organization = [
	{"name": "جمعیت امام علی", "ratings": [90,73,80,89,64], "projects": ["خرید کتاب برای کودکات مستضعف", "ساخت مدرسه ابتدایی"], "requierments": ["حسابداری", "آموزش"]},
	{"name": "جمعیت امام علی", "ratings": [90,73,80,89,64], "projects": ["خرید کتاب برای کودکات مستضعف", "ساخت مدرسه ابتدایی"], "requierments": ["حسابداری", "آموزش"]},
	{"name": "جمعیت امام علی", "ratings": [90,73,80,89,64], "projects": ["خرید کتاب برای کودکات مستضعف", "ساخت مدرسه ابتدایی"], "requierments": ["حسابداری", "آموزش"]},
	{"name": "جمعیت امام علی", "ratings": [90,73,80,89,64], "projects": ["خرید کتاب برای کودکات مستضعف", "ساخت مدرسه ابتدایی"], "requierments": ["حسابداری", "آموزش"]}
]


for (var j = 0; j < organization.length; j++) {
	var div1 = document.createElement('div');
	div1.setAttribute('class', "organization");
	var h2name = document.createElement('h3');
	h2name.innerHTML = organization[j].name;
	div1.appendChild(h2name);
	//chart colors
	var colors = ['one', 'two', 'three', 'four', 'five'];
	var TROW = 'tr', TDATA = 'td';

	var chart = document.createElement('div');
	//create the chart canvas
	var barchart = document.createElement('table');

	chart.appendChild(barchart);

	//create the bar row
	var barrow = document.createElement(TROW);
	barrow.setAttribute('class', 'bars');

	//lets add data to the chart
	for (var i = 0; i < 5; i++) {
	  //create the bar data
	  var bardata = document.createElement(TDATA);
	  var bar = document.createElement('div');
	  bar.setAttribute('class', colors[i]);
	  //bar.innerText = organization[j].ratings[i] + "%"; 
	  bar.style.height = organization[j].ratings[i] + "%";
	  bar.style.position = "absolute";
	  bar.style.width = "100%";
	  bar.style.bottom = "0";
	  bardata.appendChild(bar);
	  barrow.appendChild(bardata);
	}

	barchart.appendChild(barrow);
	chart.appendChild(barchart);
	div1.appendChild(chart);
	var projects1 = document.createElement('div');
	projects1.setAttribute('class', "projects");
	var h5title = document.createElement('h5');
	h5title.innerHTML = "آخرین پروژه‌های ثبت شده";
	projects1.appendChild(h5title);
	var ul1 = document.createElement('ul');
	for (var i = 0; i < organization[j].projects.length; i++) {
		var li1 = document.createElement('li');
		li1.innerText = organization[j].projects[i];
		ul1.appendChild(li1);
	}
	projects1.appendChild(ul1);
	div1.appendChild(projects1);
	var projects1 = document.createElement('div');
	projects1.setAttribute('class', "projects");
	var h5title = document.createElement('h5');
	h5title.innerHTML = "نیازمندی‌های غیرنقدی";
	projects1.appendChild(h5title);
	var ul1 = document.createElement('ul');
	for (var i = 0; i < organization[j].requierments.length; i++) {
		var li1 = document.createElement('li');
		li1.innerText = organization[j].requierments[i];
		ul1.appendChild(li1);
	}
	projects1.appendChild(ul1);
	div1.appendChild(projects1);
	document.getElementById("c3").appendChild(div1);
}

var benefactors = [
	{"name": "سید علی حسین‌زاده", "ratings": [90,73,80,89,64], "abilities": ["حسابداری", "آموزش"], "worked": ["جمعیت امام علی", "یاوران ایتام"]},
	{"name": "سید علی حسین‌زاده", "ratings": [90,73,80,89,64], "abilities": ["حسابداری", "آموزش"], "worked": ["جمعیت امام علی", "یاوران ایتام"]},
	{"name": "سید علی حسین‌زاده", "ratings": [90,73,80,89,64], "abilities": ["حسابداری", "آموزش"], "worked": ["جمعیت امام علی", "یاوران ایتام"]},
	{"name": "سید علی حسین‌زاده", "ratings": [90,73,80,89,64], "abilities": ["حسابداری", "آموزش"], "worked": ["جمعیت امام علی", "یاوران ایتام"]}
]

for (var j = 0; j < benefactors.length; j++) {
	var div1 = document.createElement('div');
	div1.setAttribute('class', "organization");
	var h2name = document.createElement('h3');
	h2name.innerHTML = benefactors[j].name;
	div1.appendChild(h2name);
	//chart colors
	var colors = ['one', 'two', 'three', 'four', 'five'];
	var TROW = 'tr', TDATA = 'td';

	var chart = document.createElement('div');
	//create the chart canvas
	var barchart = document.createElement('table');

	chart.appendChild(barchart);

	//create the bar row
	var barrow = document.createElement(TROW);
	barrow.setAttribute('class', 'bars');

	//lets add data to the chart
	for (var i = 0; i < 5; i++) {
	  //create the bar data
	  var bardata = document.createElement(TDATA);
	  var bar = document.createElement('div');
	  bar.setAttribute('class', colors[i]);
	  //bar.innerText = benefactors[j].ratings[i] + "%"; 
	  bar.style.height = benefactors[j].ratings[i] + "%";
	  bar.style.position = "absolute";
	  bar.style.width = "100%";
	  bar.style.bottom = "0";
	  bardata.appendChild(bar);
	  barrow.appendChild(bardata);
	}

	barchart.appendChild(barrow);
	chart.appendChild(barchart);
	div1.appendChild(chart);
	var projects1 = document.createElement('div');
	projects1.setAttribute('class', "projects");
	var h5title = document.createElement('h5');
	h5title.innerHTML = "توانایی‌ها";
	projects1.appendChild(h5title);
	var ul1 = document.createElement('ul');
	for (var i = 0; i < benefactors[j].abilities.length; i++) {
		var li1 = document.createElement('li');
		li1.innerText = benefactors[j].abilities[i];
		ul1.appendChild(li1);
	}
	projects1.appendChild(ul1);
	div1.appendChild(projects1);
	var projects1 = document.createElement('div');
	projects1.setAttribute('class', "projects");
	var h5title = document.createElement('h5');
	h5title.innerHTML = "سابقه همکاری با";
	projects1.appendChild(h5title);
	var ul1 = document.createElement('ul');
	for (var i = 0; i < benefactors[j].worked.length; i++) {
		var li1 = document.createElement('li');
		li1.innerText = benefactors[j].worked[i];
		ul1.appendChild(li1);
	}
	projects1.appendChild(ul1);
	div1.appendChild(projects1);
	document.getElementById("c5").appendChild(div1);
}