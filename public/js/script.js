var jsonObj = null;
var fname = null;

function tempData(jsonObj) { //used in ajax success
    var bookData = jsonObj.book;

    var title = bookData.title;
    var creator = bookData.creator;
    var language = bookData.language;

    /*$.each( jsonObj['book'], function( key, val) {
        $("input[name*='title'").val(key);
        //console.log(key)
    });*/

    $("input[name*='title']").val(title);
    $("input[name*='author']").val(creator);
    $("input[name*='language']").val(language);
    console.log(jsonObj.book.title);
}

$.getJSON( "listing", function(data){
    $.each( data['books'], function( key, val) {
        var file = val.author + "/" + val.title + "/" + val.author + " - " + val.title + "." + val.ext;
        console.log(file);
        $("#listing").append( "<p>" + val.author + " - " + val.title + " <a href='download/" + file + "'>Download</a></p>");
    })
});

$("#submit").click(function() {
    var fd = new FormData();
    var uploadForm = $("#file_upload")[0].files[0];
    fname = uploadForm.name;

    fd.append("my_file", uploadForm);
    //console.log(uploadForm);
    console.log(uploadForm.name);
    // Post file to server, related files: ParseEbook.py, Upload.py
    $.ajax({
        url: "upload",
        type: "POST",
        data: fd,
        processData: false,
        contentType: false,
        success: function(data) { //Return book data to user
            jsonObj = data;
            console.log(data);
            tempData(jsonObj);
        }
    });
});

$("#save").click(function() {
    var bookData = jsonObj.book;

    var ISBN = bookData.identifier;
    var ext = bookData.ext;
    var date = bookData.date;


    var fd = new FormData(document.querySelector("#confirm"));
    fd.append("ISBN", ISBN);
    fd.append("ext", ext);
    fd.append("date", date);
    fd.append("fname", fname);


    console.log(fd.title);
    console.log(fname);

    $.ajax({
        url: "edit",
        type: "POST",
        data: fd,
        processData: false,
        contentType: false
    });


});