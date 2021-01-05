$(document).ready(function() {

    // SignUp/LogIn Page
    $('.close_btn').click(function(){
        window.location.href = '/';
    });

    // mood tracker page
    $('.edit_entry').click(function(){
        window.location.href = '/mood_rating';
    });
    $('.add_entry').click(function(){
        window.location.href = '/mood_rating';
    });

    // mood randomizer
    $('.rand_submit').click(function(){
        console.log("submit clicked");
        var dropdown_val = $('#selectpicker').val();
        link_str = "mood_randomizer_" + dropdown_val;
        window.location.href = '/' + link_str;
    });
});
