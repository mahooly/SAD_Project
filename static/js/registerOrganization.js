function eduChanged() {
    var edu = document.getElementById("education");
    if (edu.value === "blank" || edu.value === "nothing") {
        document.getElementById("fieldOfEducation").style.display = "none";
    } else {
        document.getElementById("fieldOfEducation").style.display = "block";
    }
}

function participation() {
    var edu = document.getElementById("typeOfParticipation");
    if (edu.value === "atHome" || edu.value === "blank") {
        document.getElementById("tab").style.display = "none";
    } else {
        document.getElementById("tab").style.display = "block";
    }
}