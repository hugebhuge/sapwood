
const topBtn = document.getElementById("topBtn");


window.addEventListener("scroll", function () {

    if (window.scrollY > 400) {

        topBtn.style.display = "block";

    } else {

        topBtn.style.display = "none";

    }

});



topBtn.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});



const menuBtn = document.querySelector(".menu-btn");
const nav = document.querySelector("nav");

menuBtn.onclick = function(){
    nav.classList.toggle("active");
}


if(typeof GLightbox !== "undefined"){
    const lightbox = GLightbox();
}
const form = document.querySelector(".contact-form");

if(form){

    form.addEventListener("submit", function(e){

        e.preventDefault();

        const formData = new FormData(form);

        fetch("/consultation/", {
            method: "POST",
            body: formData,
            headers:{
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
.then(response => {

    console.log("STATUS:", response.status);

    return response.json();

})
.then(data => {

    
    console.log(data);



    document.getElementById("success-message").style.display="flex";

form.reset();
    

})
        .catch(error => {

            console.log(error);
            alert("خطایی رخ داد.");

        });

    });

}

const closeSuccess = document.getElementById("close-success");



closeSuccess.onclick=function(){

document.getElementById("success-message").style.display="none";

}



