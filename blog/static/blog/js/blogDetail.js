
$(document).ready(function(){
	/* Down arrow */
    $(".reply_btn").click(function(){
        
        $(this).next("form").slideToggle(750);

        $(this).fadeOut(750, "swing")
    });
});