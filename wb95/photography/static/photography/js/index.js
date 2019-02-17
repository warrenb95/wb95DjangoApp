// Set background color of the nav after you scroll past screenHeight
$(window).scroll(function(){
    // Get the screen height
    var screenHeight = $(window).height();
    
    if ($(this).scrollTop() > screenHeight-100){
        $("nav").css('background-color', '#f5f5f5');
    } else {
        $("nav").css('background-color', 'transparent');
    }
}).on("resive", function(){
    screenHeight = $(this).height();
});


$(".scroll-to").click( function(e){
    e.preventDefault();
    $('html, body').stop().animate({scrollTop: $('#me').offset().top}, 500);
});