// photo input
const imageInputs = document.querySelectorAll(".image-input");
imageInputs.forEach(function (input) {
    input.addEventListener("change", (e) => {
        console.log('changed')
        const files = e.target.files;
        const reader = new FileReader();
        const imageFile = files[0]
        reader.readAsDataURL(imageFile)
        reader.addEventListener("load", (e) => {
            console.log('loaded')
            const img = input.previousElementSibling.querySelector(".display-image")
            img.src = e.target.result
            img.alt = imageFile.name
        });
    });
})

//all inputs
const form = document.querySelector('form');
const inputs = form.querySelectorAll('input');
const image = document.querySelector('img')
const button = document.querySelector('#save-button');
const fullname = document.getElementById('fullname')

for (let i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener('input', () => {
        button.disabled = isUnchanged();
        if (button.disabled === true) {
            button.classList.add('inactive')
        } else {
            button.classList.remove('inactive')
        }
    });
}

function isUnchanged() {
    for (let i = 0; i < inputs.length; i++) {
        if (inputs[i].value !== inputs[i].defaultValue) {
            return false;
        }
    }
    return true;
}

