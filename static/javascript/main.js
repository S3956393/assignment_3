$(document).ready(function() {
    countries =  $(".ar, .be, .ca, .ie, .it, .jp, nl, .ch, .tr, .us"); 
    countries.click(function() {
        $.ajax({
            url: "/get_iso_code",
            data: JSON.stringify({'isoCode': event.target.classList[1]}),
            contentType: "application/json;charset=utf-8",
            type: "POST",
            dataType: "json",
            success: function(data) {
                $(".modal-content").replaceWith(data)
            }
        });  
        
        $('.overlay').addClass('is-open');
        return false;
    });
    
    
    $('.close-btn').on("click", function () {
        $('.overlay').removeClass('is-open');
    });
});