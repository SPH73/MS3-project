// dynamic accordion for blog/profiles/projects pages

let coll = document.getElementsByClassName("accordion-label");
let i;

for (i = 0; i < coll.length; i++) {
    coll[i].onclick = function () {
        this.classList.toggle("active");

        let content = this.nextElementSibling;

        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
        }
    }
}

// date picker for project deadlines
let today = new Date();
$('#deadline').datepicker({
    minDate: today,
    changeYear: true,
    changeMonth: true,
    showWeek: true,
    showOtherMonths: true
});

// toggle blog comment form

$(".comment-btn").click(function (event) {
    let id = event.target.id;
    let btn = this;
   
    if (btn.innerText == "Close") {
        btn.innerText = "Comment"
    } else {
        btn.innerText = "Close"
    }

    let form = event.target.nextElementSibling;
    $(form).toggleClass('hide');

})
