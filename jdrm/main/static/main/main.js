function switch_to() {
    document.getElementById("clicker1").classList.toggle("active");
    document.getElementById("clicker2").classList.toggle("active");

    if (document.getElementById("clicker2").classList.contains("active")) {
        document.getElementById("clicker2").setAttribute('onclick','');
    } else {
        document.getElementById("clicker2").setAttribute('onclick','switch_to()');
    }

    if (document.getElementById("clicker1").classList.contains("active")) {
        document.getElementById("clicker1").setAttribute('onclick','');
    } else {
        document.getElementById("clicker1").setAttribute('onclick','switch_to()');
    }

    document.getElementById("radar_char").classList.toggle("disable");
    document.getElementById("bar_char").classList.toggle("disable");
}
