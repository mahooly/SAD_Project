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

