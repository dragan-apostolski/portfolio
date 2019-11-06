$('.gallery a').simpleLightbox();

$(window).scroll(function(e){
    var scrollPos = $(document).scrollTop();
    if (scrollPos > 10){
        $(".navbar").addClass("non-transparent");
    }
    else if (scrollPos <= 10){
        $(".navbar").removeClass("non-transparent");
    }

    tabs = document.querySelector(".tabs");
    if(tabs.getBoundingClientRect().top >= 0){
        $(".tabs").removeClass("tabs-fixed");
    }
    if(tabs.getBoundingClientRect().top < 15){
        $(".tabs").addClass("tabs-fixed")

    }
});
