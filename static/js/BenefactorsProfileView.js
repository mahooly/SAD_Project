var personalData = {
    "name": "مهدیس تاجداری",
    "age": "۲۰",
    "edu": "دیپلم",
    "fieldOfEdu": "ریاضی فیزیک",
    "job": "دانشجو",
    "email": "tajdari@ce.sharif.edu",
    "photo": "images/mahdis.jpg",
	"abilities": ["حسابداری", "آموزش", "خیاطی", "روابط عمومی"],
	"week": [1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,1,1],
	"rating": [70,64,89,72,90],
	"legends": ["صداقت","تعهد","مسئولیت پذیری","وقت شناسی","علاقه به کار"]
}
var titleHeader = document.getElementById("title");
titleHeader.innerHTML = "صفحه شخصی " + personalData.name;
var photo = document.getElementById("photo");
var im = document.createElement('img');
im.setAttribute('src',personalData.photo);
photo.appendChild(im);

var personal1 = document.getElementById("personal");
var sname = document.createElement('h3');
sname.innerHTML = "نام و نام خانوادگی: " + personalData.name;
personal1.appendChild(sname);
var sage = document.createElement('h3');
sage.innerHTML = "سن: " + personalData.age;
personal1.appendChild(sage);
var sedu = document.createElement('h3');
if (personalData.edu == "ندارد")
    sedu.innerHTML = "تحصیلات: ندارد";
else
    sedu.innerHTML = "تحصیلات: " + personalData.edu + " (" + personalData.fieldOfEdu + ")";
personal1.appendChild(sedu);
var sjob = document.createElement('h3');
sjob.innerHTML = "شغل: " + personalData.job;
personal1.appendChild(sjob);
var semail = document.createElement('h3');
semail.innerHTML = "پست الکترونیک: " + personalData.email;
personal1.appendChild(semail);

//chart colors
var colors = ['one', 'two', 'three', 'four', 'five'];

//constants
var TROW = 'tr',
  TDATA = 'td';

var chart = document.createElement('div');
//create the chart canvas
var barchart = document.createElement('table');

chart.appendChild(barchart);

//create the bar row
var barrow = document.createElement(TROW);

//lets add data to the chart
for (var i = 0; i < personalData.rating.length; i++) {
  barrow.setAttribute('class', 'bars');
  //create the bar data
  var bardata = document.createElement(TDATA);
  var bar = document.createElement('div');
  bar.setAttribute('class', colors[i]);
  bar.innerText = personalData.rating[i] + "%"; 
  bar.style.height = personalData.rating[i] + "%";
  bar.style.position = "absolute";
  bar.style.width = "100%";
  bar.style.bottom = "0";
  bardata.appendChild(bar);
  barrow.appendChild(bardata);
}

//create legends
var legendrow = document.createElement(TROW);
var legend = document.createElement(TDATA);
legend.setAttribute('class', 'legend');
legend.setAttribute('colspan', personalData.rating.length);

//add legend data
for (var i = 0; i < personalData.rating.length; i++) {
  var legbox = document.createElement('span');
  legbox.setAttribute('class', 'legbox');
  var barname = document.createElement('span');
  barname.setAttribute('class', colors[i] + ' xaxisname');
  var bartext = document.createElement('span');
  bartext.innerText = personalData.legends[i];
  legbox.appendChild(barname);
  legbox.appendChild(bartext);
  legend.appendChild(legbox);
}
barrow.appendChild(legend);
barchart.appendChild(barrow);
barchart.appendChild(legendrow);
chart.appendChild(barchart);
document.getElementById('chart').innerHTML = chart.outerHTML;

var ab = document.getElementById("abilities");
for (var i = 0; i < personalData.abilities.length; i++) {
    var s = document.createElement('span');
    s.setAttribute('class', 'abilitySpan');
    s.style.display = "block";
    s.style.margin = "2px 20px 2px 0";
    s.innerText = personalData.abilities[i];
    s.value = 1;
    s.onclick = function() {
        if (this.value == 1) {
            this.style.backgroundColor = "rgb(4,80,255)";
            this.value = 2;
        }
        else {
            this.style.backgroundColor = "rgba(0,0,0,0.4)";
            this.value = 1;
        }
    }
    ab.appendChild(s);
}

var week = {
    "day": ["شنبه", "یکشنبه", "دوشنبه" ,"سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه"],
    "hour": [" ", "۸-۱۰", "۱۰-۱۲", "۱۲-۱۵", "۱۵-۱۷"]
}
var dd = document.getElementById('weeklyfreetime');
var table = document.createElement('table');
table.setAttribute('class','weektable');
var thead = document.createElement('tr');
for (var i = 0; i < week.hour.length; i++) {
    var th = document.createElement('td');
    th.innerText = week.hour[i];
    thead.appendChild(th);
}
table.appendChild(thead);
for (var i = 0; i < 7; i++) {
    var row = document.createElement('tr');
    var data = document.createElement('td');
    data.innerText = week.day[i];
    row.appendChild(data);
    for (var j = 0; j < 4; j++) {
        var d = document.createElement('td');
        var span = document.createElement('span');
        var id = i*4+j;
        span.id = id;
        if (personalData.week[id] == 0) {
            span.setAttribute('class', 'free');
            span.value = 1;
            span.onclick = function() {
                if (this.value == 1) {
                    this.style.backgroundColor = "rgb(15,157,242)";
                    this.value = 2;
                }
                else {
                    this.style.backgroundColor = "rgb(191,215,157)";
                    this.value = 1;
                }
            };
        }
        if (personalData.week[id] == 1) {
            span.setAttribute('class', 'busy');
        }
        d.appendChild(span);
        row.appendChild(d);
    }
    table.appendChild(row);
}
dd.appendChild(table);