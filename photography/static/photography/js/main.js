$(document).ready(function(){
    
    /* Page fade in */
    $("body").css("display", "none");
    $("body").fadeIn(750);
    
    /* Fade out when link is pressed */
    $("a.trans").click(function(event){
        event.preventDefault();
        linkLocation = this.href;
        $("body").fadeOut(750, redirectPage);      
    });
    
    /* Go to the link page */
    function redirectPage() {
        window.location = linkLocation;
    }
    
    /* Drop down slide down */
    $("#humburger").click(function(){
        $(".drop-content").slideToggle(750, "swing");
        
        /* Change hamburger is-active when clicked */
        if($(this).hasClass("is-active")){
            $(this).removeClass("is-active");
        } else {
            $(this).addClass("is-active");
        }
    });
    
    /* Slide menu up if scroll */
    $(window).scroll(function(){
        $(".drop-content").slideUp(750, "swing");
        $("#humburger").removeClass("is-active");
    });
    
    /* Sticky menu */
    $(window).scroll(function(){
        if ( $(window).pageYOffset >= $("nav").offsetTop ) {
            $("nav").addClass("sticky");
        } else {
             $("nav").removeClass("sticky");
        }
    });
    
    /* Down arrow */
    $(".show-toggle").click(function(){
        $(this).fadeOut(500, function(){
            $(this).toggleClass("rotate animated infinite bounce slow");
        });
        
        $(this).next(".more-text").slideToggle(750);
        
        if($("footer").hasClass("bottom")){
            $("footer").toggleClass("bottom");
        }
        
        $(this).fadeIn(500);
    });
    
});
