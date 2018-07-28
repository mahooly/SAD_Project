function clicked(a,b) {
    document.getElementById("a1").value = a + "-" + b;
    document.getElementById("form1").submit();
}
var ll = document.getElementById("uls");
var lis = [];
while(ll.hasChildNodes()) {
    lis.unshift(ll.childNodes[0].value);
    console.log(ll.childNodes[0].value);
    ll.removeChild(ll.childNodes[0]);
}
for (var k = 0; k < lis.length; k++) {
    for (i = 1; i <= 7; i++) {
        var j;
        for (j = 1; j <= 4; j++) {
            if (document.getElementById('a' + lis[k] + 'b' + ((i - 1) * 4 + j - 1)).checked === true) {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(150,150,150)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 3;
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.width = "100%";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.height = "10px";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.borderRadius = "10px";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.display = "inline-block";
            } else {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(211,233,158)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 2;
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.width = "100%";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.height = "10px";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.borderRadius = "10px";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.display = "inline-block";
            }
        }
    }
}

function deleteReq(e) {
    document.getElementById("delete"+e).style.display="block";
}

function popdownDeleteReq(e) {
    document.getElementById("delete"+e).style.display="none";
}

document.getElementById("not").addEventListener('click', function (e) {
    e.preventDefault()
});