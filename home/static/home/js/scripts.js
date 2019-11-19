let scrollPosition = 0;

$('.gallery a').simpleLightbox();

$('#navbarResponsive').on('shown.bs.collapse', function() {
    $('.navbar').addClass('non-transparent');
});

$('#navbarResponsive').on('hidden.bs.collapse', function () {
    if (scrollPosition == 0) {
        $('.navbar').removeClass('non-transparent');
    }
});

$(window).scroll(function(){
    let scrollPos = $(document).scrollTop();
    scrollPosition = scrollPos;
    if (scrollPos > 10){
        $(".navbar").addClass("non-transparent");
    }
    else if (scrollPos <= 10){
        $(".navbar").removeClass("non-transparent");
    }

    let tabs = document.querySelector(".tabs");
    if(tabs.getBoundingClientRect().top >= 0){
        $(".tabs").removeClass("tabs-fixed");
    }
    if(tabs.getBoundingClientRect().top < 15){
        $(".tabs").addClass("tabs-fixed")

    }
});
