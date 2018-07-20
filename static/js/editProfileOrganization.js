var cities = ["تهران","مشهد","اصفهان","شیراز"];
var sel = document.getElementById('city');
for (var i=0;i<cities.length;i++) {
	var opt = document.createElement('option');
	opt.setAttribute('value', cities[i]);
	opt.innerHTML = cities[i];
	sel.appendChild(opt);
}