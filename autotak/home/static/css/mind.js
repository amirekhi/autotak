document.querySelector('#btn').onclick = function() {
    document.querySelector('#slider').style.right = 0
}
document.querySelector('#close').onclick = function() {
    document.querySelector('#slider').style.right = "-310px"
}

window.onscroll = function() {
    if (window.scrollY >= 300){
        document.querySelector('#container2').style.transform= 'translateX(0) translateY(-100px)'
    }

}