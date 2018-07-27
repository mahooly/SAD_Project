var fields = {
  "data": ["پیشنهاد همکاری", "امتیازدهی", "کمک مالی", "ویرایش حساب کاربری"]
};
var sel = document.getElementById("field");
var opt = document.createElement('option');
opt.setAttribute('value', "blank");
opt.innerText = "زمینه فعالیت";
sel.appendChild(opt);
for (var i = 0; i < fields.data.length; i++) {
  opt = document.createElement('option');
  opt.setAttribute('value',fields.data[i]);
  opt.innerText = fields.data[i];
  sel.appendChild(opt);
}

function rate (e1,e2) {
  var id1 = "button" + e1;
  for (var i = 1; i <= e2; i++) {
    document.getElementById(id1+i).style.backgroundColor = "#E0B0FF";
  }
  for (i = e2+1; i < 6; i++) {
    document.getElementById(id1+i).style.background = "none";
  }
}

for (i = 1; i <=7; i ++) {
    var j;
    for (j = 1; j <= 4; j ++ ) {
        if (document.getElementById('a' + ((i-1)*4+j-1)).checked === true) {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(150,150,150)";
            document.getElementById(i + "" + j).style.display = "inline-block";
            document.getElementById(i + "" + j).style.width = "100%";
            document.getElementById(i + "" + j).style.heigth = "30px";
        } else {
            document.getElementById(i + "" + j).style.backgroundColor = "rgb(211,233,158)";
            document.getElementById(i + "" + j).style.display = "inline-block";
            document.getElementById(i + "" + j).style.width = "100%";
            document.getElementById(i + "" + j).style.height = "30px";

        }
    }
}

function popdownregisters(id) {
	document.getElementById("testreg"+id).style.display = "none";
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
