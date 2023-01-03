document.getElementById("simplify_button").addEventListener("click", function (e) {
    e.preventDefault();
    let xhr = new XMLHttpRequest();
    let data = new FormData();
    let csrftoken = document.querySelector("input[name=csrfmiddlewaretoken]").value;
    data.append("url", document.querySelector("input[name=url]").value);
    xhr.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.querySelector(".result_field").classList.add("show");
            document.getElementById("result").innerHTML = xhr.responseText;
            if(xhr.responseText.startsWith("http")){
                document.getElementById("result").href = xhr.responseText;
                document.getElementById("result").classList.add("content");
            }else{
                if(document.getElementById("result").classList.contains("content")){
                    document.getElementById("result").classList.remove("content");
                }
                if(document.getElementById("result").hasAttributes("href")){
                    document.getElementById("result").removeAttribute("href");
                }
            }
        }
    };
    xhr.open("POST", "simplify", true);
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.send(data);
});