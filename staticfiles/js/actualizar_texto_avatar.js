// This updates de avatar but is not working properly
const fileInput = document.querySelector('input[type="file"]');

fileInput.addEventListener('change', (event)=>{
    const file = event.target.files[0];
    const image = document.querySelector('#avatar');

    if (file && file.type.includes('image')){
        const url = URL.createObjectURL(file);
        image.src = url;
    }
})

// This updates the name
const real_nameInput = document.getElementById('id_real_name');
const real_nameOutput = document.getElementById('real_name');

real_nameInput.addEventListener('input', (event)=>{
    real_nameOutput.textContent = event.target.value;
});