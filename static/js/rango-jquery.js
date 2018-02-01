$(document).ready(function () {
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });


    $(document).on( 'click', ".ouch" , function(event) {
        alert("You clicked me! ouch!");
    });

    $("p").hover( function() {
        $(this).css('color', 'red');
    },
    function() {
        $(this).css('color', 'black');
    });

    $(document).on('click', "#about-btn", function(event) {
        msgstr = $("#msg").html()
        msgstr = msgstr + "ooo"
        $("#msg").html(msgstr)
    });
});
