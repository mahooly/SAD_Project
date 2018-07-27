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
  opt.setAttribute('value',i);
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

var reqs = document.getElementById("tempUl");
var reqs1 = document.getElementById("tempUl1");
var req = [];
var req1 = [];
for (i = 0 ; i < reqs.childNodes.length; i ++ ) {
    req.unshift(reqs.childNodes[i].value);
}
for (i = 0 ; i < reqs1.childNodes.length; i ++ ) {
    req1.unshift(reqs1.childNodes[i].value);

}
for (i = 0 ; i < req1.length; i ++) {
    document.getElementById("not"+req1[i]).addEventListener("click", function(event){
		event.preventDefault()
	});
}

for (var k = 0; k < req.length; k ++) {
    console.log(req[k]);
    for (i = 1; i <= 7; i++) {
        var j;
        for (j = 1; j <= 4; j++) {
            if (document.getElementById('a' + req[k] + 'b' + ((i - 1) * 4 + j - 1)).checked === true) {
                document.getElementById('a' + req[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(120,120,120)";

            } else {
                document.getElementById('a' + req[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(211,233,158)";


            }
            document.getElementById('a' + req[k] + 'a' + i + "" + j).style.display = "inline-block";
            document.getElementById('a' + req[k] + 'a' + i + "" + j).style.width = "100%";
            document.getElementById('a' + req[k] + 'a' + i + "" + j).style.height = "10px";
            document.getElementById('a' + req[k] + 'a' + i + "" + j).style.borderRadius = "5px";
        }
    }
}

function popdownregisters(id) {
	document.getElementById("testreg"+id).style.display = "none";
}
function showRemove(id) {
	document.getElementById("testreg"+id).style.display = "block";
}
function f(id) {
    document.getElementById(id).addEventListener("click", function(event){
        event.preventDefault()
    });
}