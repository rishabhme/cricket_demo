new WOW().init();

//$('#navbarContent').hide();
$('#navbartoggle').click(function () {
    $('#navbarContent').toggleClass('show');
    $(this).toggleClass('open');
});

//scrool menu js
$(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll >= 100) {
        $("#navbar").addClass("headercolor");
    } else {
        $("#navbar").removeClass("headercolor");
    }
});
