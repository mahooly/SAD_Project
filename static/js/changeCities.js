var templistt = document.getElementById("templist");
while (templistt.hasChildNodes()) {
    addd(templistt.childNodes[0].id);
    templistt.removeChild(templistt.childNodes[0]);
}

function addd(candidate1) {
    var ul = document.getElementById("dynamiclist");
    var li2 = document.createElement("li");
    var span = document.createElement("SPAN");
    span.id = candidate1;
    span.style.marginBottom = "0px";
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.onclick = function() {
            document.getElementById("username").value = this.id;
            document.getElementById("type").value = 2;
            document.getElementById("username").form.submit();
        };
    span.appendChild(txt);
    li2.appendChild(span);
    //li.setAttribute('id',candidate1);
    li2.appendChild(document.createTextNode(candidate1));
    ul.appendChild(li2);
}