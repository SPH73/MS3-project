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
    dateFormate: "dd-mm-yy",
    changeYear: true,
    changeMonth: true,
    showWeek: true,
    showOtherMonths: true
});

// toggle blog comment form
$(".comment-btn").click(function () {
    $('.comment-form').toggleClass("hidden");
});