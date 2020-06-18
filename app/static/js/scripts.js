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

$('.comment-btn').on('click', function () {
    $('.form-box').toggle();

})

// function changeValue() {

//     let btn = document.getElementsByClassName('comment-btn');

//     if (btn.value == "Hide") {
//         btn.value = "Comment";
//         btn.innerHTML = "Comment";
//     } else {
//         btn.value = "Hide";
//         btn.innerHTML = "Hide";
//     }
// }

function changeValue() {

    let btn = document.getElementById('blog-comment-btn');

    if (btn.textContent === "Hide") {
        btn.textContent = "Comment";
    } else {
        btn.textContent = "Hide";

    }
}
// $('.close-btn').on('click', function () {
//     $('.form-box').hide();
// })