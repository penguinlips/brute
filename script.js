function Brute(){
    User = document.getElementById("uname").value;
    Pass = document.getElementById("pass").value;
    if (User == "penguinlips" && Pass == "pass@123"){
        window.open("https://penguinlips.github.io/ansan_mathew/index.html");
}
}

function Clear(){
    document.getElementById("uname").value="";
    document.getElementById("pass").value="";
}