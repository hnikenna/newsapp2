var scrollBtns = document.getElementsByClassName('scroll-btn')
var scrolling = false

function Scroller() {
//    alerT('', 'Scrolling..')
    if (scrolling === true) {
        window.scrollBy(0,10);
        scrolldelay = setTimeout(Scroller,100);
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            // you're at the bottom of the page
//                console.log('scope5')
                scrolling = false
                scrollBtn.innerHTML = '<b>Auto-Scroll</b>'
            }

    }
}



for (var i=0; i<scrollBtns.length; i++){
    scrollBtns[i].addEventListener('click', function (e){
    //    console.log('scope1')
        if (scrolling === false) {
    //        console.log('scope2')
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                // you're at the bottom of the page
    //                console.log('scope4')
                    scrolling = false
                    this.innerHTML = '<b>Auto-Scroll</b>'
                } else {
    //                console.log('scope3')
                    scrolling = true
                    this.innerHTML = '<b style="color: red;">Stop</b>'
                    Scroller()
                }
        } else {
            scrolling = false
            this.innerHTML = '<b>Auto-Scroll</b>'
        }
    })
}
