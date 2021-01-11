$(document).ready(function() {

    // SignUp/LogIn Page
    $('.close_btn').click(function() {
        window.location.href = '/';
    });

    // mood tracker page
    $('.edit_entry').click(function() {
        window.location.href = '/mood_rating';
    });
    $('.add_entry').click(function() {
        window.location.href = '/mood_rating';
    });

    // mood randomizer
    $('.rand_submit').click(function() {
        var dropdown_val = $('#selectpicker').val();
        window.location.href = `/mood_randomizer_${dropdown_val}`;
    });
});