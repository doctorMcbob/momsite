//this is a script
function contact_form_submit() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var msg = document.getElementById("message").value;
    alert("here")
    xhttp.open("POST", "/email", true);
    xhttp.setRequestHeader("name", name);
    xhttp.setRequestHeader("email", email);
    xhttp.setRequestHeader("message", msg);
    xhttp.send();
    return false;
}
