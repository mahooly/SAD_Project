var isLogedIn = true;
var topmenu = document.getElementById("topmenu");
var personal = {
	"photo": "../static/images/pouyan.jpg",
	"name": "پویان",
	"lastname": "شیرزادیان",
	"isOrg": true,
	"isBen": false
}

if (isLogedIn) {
	var container = document.createElement('div');
	container.setAttribute('class', "container");
	var photo = document.createElement('div');
	photo.setAttribute('class', "topPhoto");
	var image = document.createElement('img');
	image.setAttribute('src', personal.photo);
	photo.appendChild(image);
	container.appendChild(photo);
	var name1 = document.createElement('div');
	name1.setAttribute('class', "topmenuelements");
	var aname = document.createElement('a');
	aname.setAttribute('class', "name");
	if (personal.isOrg)
		aname.setAttribute('href', "personalProfileOrganization.html");
	else if (personal.isBen)
		aname.setAttribute('href', "personalProfileBenefactor.html");
	aname.innerText = personal.name + " " + personal.lastname;
	name1.appendChild(aname);
	container.appendChild(name1);
	var exit1 = document.createElement('div');
	exit1.setAttribute('class', "topmenudate");
	var aexit = document.createElement('a');
	aexit.setAttribute('href', "index.html");
	aexit.innerText = "خروج";
	exit1.appendChild(aexit);
	container.appendChild(exit1);
	var logo = document.createElement('div');
	logo.setAttribute('class', "logo");
	var image = document.createElement('img');
	image.setAttribute('src', "/images/logo.jpg");
	logo.appendChild(image);
	container.appendChild(logo);
	topmenu.appendChild(container);
}
else {
	var container = document.createElement('div');
	container.setAttribute('class', "container");
	var matn1 = document.createElement('div');
	matn1.setAttribute('class', "topmenudate");
	var h = document.createElement('h3');
	h.innerText = "شما هنوز وارد نشده‌اید،";
	matn1.appendChild(h);
	container.appendChild(matn1);
	var enter = document.createElement('div');
	enter.setAttribute('class', "topmenudate");
	var button1 = document.createElement('button');
	button1.setAttribute('onclick', "popup()");
	button1.innerText = "ورود";
	enter.appendChild(button1);
	container.appendChild(enter);
	var reg = document.createElement('div');
	reg.setAttribute('class', "topmenudate");
	var button1 = document.createElement('button');
	button1.setAttribute('onclick', "popupregister()");
	button1.innerText = "ثبت نام";
	reg.appendChild(button1);
	container.appendChild(reg);
	topmenu.appendChild(container);
}

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
	});
	document.getElementById("buttonreg2").addEventListener("click", function(event){
		event.preventDefault()
	});
	document.getElementById("button2").addEventListener("click", function(event){
		event.preventDefault()
	});
}
f();

var div1 = document.getElementById('nav');
var ul1 = document.createElement('ul');
if (isLogedIn && personal.isOrg) {
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "create_project");
	a1.innerText = "ثبت پروژه جدید";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	
	var li2 = document.createElement('li'); 
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu1");
	var a1 = document.createElement('a');
	a1.innerText = "گزارش";
	li2.appendChild(a1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "#");
	a1.innerText = "وضعیت تامین مالی پروژه‌ها";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "#");
	a1.innerText = "پیشنهادهای ارسال‌ شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "#");
	a1.innerText = "پیشنهادهای دریافت شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchAbilities.html");
	a1.innerText = "جستجوی نیکوکاران";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "editProfileOrganization.html");
	a1.innerText = "ویرایش حساب کاربری";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}
else if (isLogedIn && personal.isBen) {
	var li2 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.innerText = "جستجو";
	li2.appendChild(a1);
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu");
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchProject.html");
	a1.innerText = "جستجوی پروژه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchRequirement.html");
	a1.innerText = "جستجوی نیازمندی";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);

	var li2 = document.createElement('li'); 
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu");
	var a1 = document.createElement('a');
	a1.innerText = "گزارش";
	li2.appendChild(a1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "#");
	a1.innerText = "پیشنهادهای ارسال‌ شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "#");
	a1.innerText = "پیشنهادهای دریافت شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "editProfileBenefactor.html");
	a1.innerText = "ویرایش حساب کاربری";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}
else if (isLogedIn) {
	var li2 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.innerText = "جستجو";
	li2.appendChild(a1);
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu1");
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchProject.html");
	a1.innerText = "جستجوی پروژه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchAbilities.html");
	a1.innerText = "جستجوی نیکوکاران";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "searchRequirement.html");
	a1.innerText = "جستجوی نیازمندی";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "reportsForAdmin.html");
	a1.innerText = "گزارش‌ها";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);

	var li2 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.innerText = "ثبت کاربر جدید";
	li2.appendChild(a1);
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu");
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "registerBenefactor.html");
	a1.innerText = "نیکوکار";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "registerOrganization.html");
	a1.innerText = "موسسه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "reportsForAdmin.html");
	a1.innerText = "لیست کاربران در انتظار تایید ";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}