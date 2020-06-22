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

$('#due_date').datepicker({
    minDate: today,
    changeYear: true,
    changeMonth: true,
    showWeek: true,
    showOtherMonths: true
});

// toggle blog comment form

$(".comment-btn").click(function (event, target) {

    let id = event.target.id;
    console.log(id, event, target);

    let btn = this;

    if (btn.innerText == "Comment") {
        btn.innerText = "Close"
    } else {
        btn.innerText = "Comment"
    }

    let form = event.target.nextElementSibling;
    console.log(form, event, target);
    $(form).toggleClass('show');
    $(form).toggleClass('hide');


})
$(".msg-btn").click(function (event, target) {

    let id = event.target.id;
    console.log(id, event, target);

    let btn = this;

    if (btn.innerText == "Message") {
        btn.innerText = "Close"
    } else {
        btn.innerText = "Message"
    }

    let form = event.target.nextElementSibling;
    console.log(form, event, target);
    $(form).toggleClass('show');
    $(form).toggleClass('hide');


})

function openTab(evt, tabName) {
    // Declare all variables
    let i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}