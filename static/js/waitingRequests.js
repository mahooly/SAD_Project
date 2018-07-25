function clicked(a,b) {
    document.getElementById("a1").value = a + "-" + b;
    document.getElementById("form1").submit();
}

for (var k = 0; k < lis.length; k++) {
    for (i = 1; i <= 7; i++) {
        var j;
        for (j = 1; j <= 4; j++) {
            if (document.getElementById('a' + lis[k] + 'b' + ((i - 1) * 4 + j - 1)).checked === true) {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(150,150,150)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 3;
            } else {
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).style.backgroundColor = "rgb(211,233,158)";
                document.getElementById('a' + lis[k] + 'a' + i + "" + j).value = 2;
            }
        }
    }
}