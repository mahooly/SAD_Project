var topmenu = document.getElementById("topmenu");

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

var mm = document.getElementById("checkspann").className;
var div1 = document.getElementById('nav');
var ul1 = document.createElement('ul');
if (mm === "2") {
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/");
	a1.innerText = "صفحه اصلی";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/create_project");
	a1.innerText = "ثبت پروژه جدید";
	li1.appendChild(a1);
	ul1.appendChild(li1);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/submit_requirement");
	a1.innerText = "ثبت نیازمندی جدید";
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
	a1.setAttribute('href', "/waiting_requests");
	a1.innerText = "پیشنهادهای دریافت شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_abilities");
	a1.innerText = "جستجوی نیکوکاران";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/editprofileorg");
	a1.innerText = "ویرایش حساب کاربری";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}
else if (mm === "3") {
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/");
	a1.innerText = "صفحه اصلی";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);

	var li2 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.innerText = "جستجو";
	li2.appendChild(a1);
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu");
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_projects");
	a1.innerText = "جستجوی پروژه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_requirements");
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
	a1.setAttribute('href', "/waiting_requests");
	a1.innerText = "پیشنهادهای دریافت شده";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);
	
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/editprofileben");
	a1.innerText = "ویرایش حساب کاربری";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}
else if (mm === "4") {
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/");
	a1.innerText = "صفحه اصلی";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);

	var li2 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.innerText = "جستجو";
	li2.appendChild(a1);
	var ol1 = document.createElement('ol');
	ol1.setAttribute('class', "innermenu1");
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_projects");
	a1.innerText = "جستجوی پروژه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_abilities");
	a1.innerText = "جستجوی نیکوکاران";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/search_requirements");
	a1.innerText = "جستجوی نیازمندی";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/reports");
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
	a1.setAttribute('href', "/register_benefactor");
	a1.innerText = "نیکوکار";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/register_organization");
	a1.innerText = "موسسه";
	li1.appendChild(a1);
	ol1.appendChild(li1);
	li2.appendChild(ol1);
	ul1.appendChild(li2);

	var li1 = document.createElement('li');
	var a1 = document.createElement('a');
	a1.setAttribute('href', "/waiting_registers");
	a1.innerText = "لیست کاربران در انتظار تایید ";
	li1.appendChild(a1);
	ul1.appendChild(li1);
	div1.appendChild(ul1);
}