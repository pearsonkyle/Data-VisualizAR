var slider = document.getElementById("myRange");
var model = document.getElementById("model");
// output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    let scale = model.getAttribute("scale");
    scale.x = this.value/100.;
    scale.y = this.value/100.;
    scale.z = this.value/100.;
    model.setAttribute(scale);
    console.log(scale);
}