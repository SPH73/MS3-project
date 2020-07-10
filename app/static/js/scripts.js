// dynamic accordion for blog/profiles/projects pages
// CREDIT Combination of Youtube tutorials to achieve accordion functionalty. 
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


    let btn = this;

    if (btn.innerText == "Comment") {
        btn.innerText = "Close"
    } else {
        btn.innerText = "Comment"
    }

    let form = event.target.nextElementSibling;

    $(form).toggleClass('show');
    $(form).toggleClass('hide');


})
$(".msg-btn").click(function (event, target) {

    let id = event.target.id;


    let btn = this;

    if (btn.innerText == "Message") {
        btn.innerText = "Close"
    } else {
        btn.innerText = "Message"
    }

    let form = event.target.nextElementSibling;

    $(form).toggleClass('show');
    $(form).toggleClass('hide');


})
// CREDIT -An adaption of W3Schools how to do tabs

function openTab(event, tabName) {
    // Declare all variables
    let i, tabcontent, tablink;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.querySelectorAll(".tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablink" and remove the class "active"
    tablink = document.querySelectorAll(".tablink");

    for (i = 0; i < tablink.length; i++) {
        tablink[i].className = tablink[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
}


// taken from pythonise.com
// saves the filesize as a cookie
function filesize(elem) {
    document.cookie = `filesize=${elem.files[0].size}`
}