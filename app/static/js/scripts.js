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

// dynamic input field for project form pieces
$("#add-piece").click(function () {
    let addPiece = '<input class="form-control form-control-lg" id="pieces-0-piece" name="pieces-0-piece" type="text" value="">';
    $('input').append(addPiece);
})