document.querySelector('form').addEventListener('submit', function(e) {
    var username = document.querySelector('input[name="username"]').value;
    var password = document.querySelector('input[name="password"]').value;

    if (username === "" || password === "") {
        e.preventDefault();
        alert("Please fill in all fields!");
    }
});
