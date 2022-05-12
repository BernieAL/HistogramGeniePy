window.onload = ()=>{
    t = document.createElement('p')
    t.innerText = "HELLO"


    color_hexCode = "#####"

    parent_color_box_container = document.querySelector('.box-container')
    console.log(parent_color_box_container)
    /*Make these and append to parent_color_box
        <div class="color-container">
			<div class="color color--1"></div>
			<h2 class="hex">#f08c00</h2>
		</div>
    */
    color_class_innerDiv = document.createElement('div')
    color_class_innerDiv.className = "color color--1"
    
    hex_class_label = document.createElement('h2')
    hex_class_label.class = "hex"
    hex_class_label.innerText = color_hexCode
    
    color_container = document.createElement('div')
    color_container.className = "color-container"
    
    color_container.appendChild(color_class_innerDiv)
    color_container.appendChild(hex_class_label)

    parent_color_box_container.appendChild(color_container)
    
}
