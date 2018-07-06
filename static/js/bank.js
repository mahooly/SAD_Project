function movetoNext(current, nextFieldID) {
	if (current.value.length >= current.maxLength) {
		document.getElementById(nextFieldID).focus();
	}
}

var receiver = {"name": "جمعیت امام علی", "site": "emamali.ir"};
var payment1 = 1200000;

var name1 = document.createElement('span');
name1.innerHTML = receiver.name;
document.getElementById("name").appendChild(name1);
var payment2 = document.createElement('span');
payment2.innerHTML = payment1;
document.getElementById("payment").appendChild(payment2);
var site1 = document.createElement('span');
site1.innerHTML = receiver.site;
document.getElementById("site").appendChild(site1);

