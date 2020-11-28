$(document).ready(function() {
    $('.edit_entry').click(function(){
        window.location.href = '/mood_rating';
    });
    $('.add_entry').click(function(){
        window.location.href = '/mood_rating';
    });
    $('.rand_submit').click(function(){
        console.log("submit clicked");
        var dropdown_val = $('.selectpicker').val();
        link_str = "mood_randomizer_" + dropdown_val;
        alert(link_str);
        console.log(link_str);
        window.location.href = '/' + link_str;
    });
});
