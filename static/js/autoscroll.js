var scrollBtns = document.getElementsByClassName('scroll-btn')
var scrolling = false

function Scroller(scrollBtn) {
//    alerT('', 'Scrolling..')
    if (scrolling === true) {

        window.scrollBy(0,10);
        console.log(scrollBtn)
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            // you're at the bottom of the page
                console.log('scope5')
                scrolling = false
                scrollBtn.innerHTML = '<b>Auto-Scroll</b>'
            } else {scrolldelay = setTimeout(function(){Scroller(scrollBtn)},100);}

    }
}



for (var i=0; i<scrollBtns.length; i++){
    scrollBtns[i].addEventListener('click', function (e){
        console.log('scope1')
        if(this.id == 'mobile-scroll'){
            this.mobile = true
        } else {
            this.mobile = false

        }
        if (scrolling === false) {
            console.log('scope2')
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                // you're at the bottom of the page
                    console.log('scope4')
                    scrolling = false
                    this.innerHTML = '<b>Auto-Scroll</b>'
                } else {
                    console.log('scope3')
                    scrolling = true
                    if(this.mobile){
                        this.innerHTML = '<b style="color: #DFFF40;">Stop</b>'
                    } else {
//                    For Desktop
                        this.innerHTML = '<b style="color: red;">Stop</b>'
                    }

                    Scroller(this)
                }
        } else {
            console.log('scope6')
            scrolling = false
            this.innerHTML = '<b>Auto-Scroll</b>'
        }
    })
}
