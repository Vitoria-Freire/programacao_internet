$(document).ready(function(){
    $('p').hover(function() {
        $(this).addClass('newcolor'); 
    },
    function(){
        $(this).removeClass('newcolor');
    });
});