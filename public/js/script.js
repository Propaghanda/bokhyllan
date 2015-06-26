$.getJSON( "index.json", function(data){
    $.each( data['books'], function( key, val) {
        $("#listing").append( "<p>"+val.author+" - "+val.title+"</p>" );
    })
});