var scrollBtns = document.getElementsByClassName('scroll-btn')
var scrolling = false
var scrollinfo = true
function Scroller(scrollBtn) {
//    alerT('', 'Scrolling..')
    if (scrolling === true) {

        if(window.location.pathname === '/') {
            if(scrollinfo) {

//                scrolldelay = setTimeout(function(){alerT('', 'Align article to page center for better view', '#3F1B3C')},50)
                scrollinfo = false
            }
            window.scrollBy(0,475);
        } else {window.scrollBy(0,1);}

//        console.log(scrollBtn)
        if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
            // you're at the bottom of the page
//                console.log('scope5')
                scrolling = false
                scrollinfo = true
                scrollBtn.innerHTML = '<i class="fa fa-flash" style="color: white; font-size: 150%;"></i>'
            } else {
                if(window.location.pathname === '/') {
                    scrolldelay = setTimeout(function(){Scroller(scrollBtn)},3000);
                    } else {
                        scrolldelay = setTimeout(function(){Scroller(scrollBtn)},50);
                    }

            }

    }
}



for (var i=0; i<scrollBtns.length; i++){
    scrollBtns[i].addEventListener('click', function (e){
//        console.log('scope1')
        if(this.id == 'mobile-scroll'){
            this.mobile = true
        } else {
            this.mobile = false

        }
        if (scrolling === false) {
//            console.log('scope2')
            if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
                // you're at the bottom of the page
//                    console.log('scope4')
                    scrolling = false
                    scrollinfo = true
                    this.innerHTML = '<i class="fa fa-flash" style="color: white; font-size: 150%;"></i>'
                } else {
//                    console.log('scope3')
                    scrolling = true
                    if(this.mobile){
                        this.innerHTML = '<i class="fa fa-ban" style="color: white; font-size: 150%; color: #DFFF40;"></i>'
                    } else {
//                    For Desktop
                        this.innerHTML = '<i class="fa fa-ban" style="color: white; font-size: 150%; color: #DFFF40;"></i>'
                    }

                    Scroller(this)
                }
        } else {
//            console.log('scope6')
            scrolling = false
            scrollinfo = true
            this.innerHTML = '<i class="fa fa-flash" style="color: white; font-size: 150%;"></i>'
        }
    })
}
