
var person={
"name": "مهدیس تاجداری", "type": "نیکوکار", "linkk": "benefactorsProfileView.html"};
var temp=document.createElement('a');
temp.innerHTML=person.name+", "+person.type;
temp.setAttribute("href",person.linkk);

var pic=document.createElement('img');
pic.setAttribute("src","images/mahdis.jpg");
var profile=document.getElementById("profile");

profile.appendChild(pic);
profile.appendChild(temp);




function rate (e1,e2) {
  var id1 = "button" + e1;
  for (var i = 1; i <= e2; i++) {
    document.getElementById(id1+i).style.backgroundColor = "#E0B0FF";
  }
  for (var i = e2+1; i < 6; i++) {
    document.getElementById(id1+i).style.background = "none";
  }
}


