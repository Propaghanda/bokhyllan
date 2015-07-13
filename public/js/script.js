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

function linkText(type, id) {
    var a = document.createElement('a');
    a.className = "btn btn-primary "+type;
    a.role = "button";
    a.href = type+"/"+id;
    a.id = id;
    a.title = type;
    a.appendChild(document.createTextNode(type));
    return a;
}

function getListing() {

    document.getElementById("listing").innerHTML = "";
    $.getJSON( "listing", function(data){
        $.each( data['books'], function( key, val) {
            var file = val.author + "/" + val.title + "/" + val.author + " - " + val.title + "." + val.ext;
            console.log(file);

            var tr = document.createElement('tr');

            var keys = [val.id, val.author, val.title, val.language];

            for (key of keys) {
                var td = document.createElement('td');
                td.appendChild(document.createTextNode(key));
                tr.appendChild(td);
            
            };

            var td = document.createElement('td');
            var img = document.createElement('img');
            img.src = "image/"+val.id;
            td.appendChild(img);
            tr.appendChild(td);

            document.getElementById('listing').appendChild(tr);

        })
    });

}

getListing();


$("#submit").click(function() {
    var fd = new FormData();
    var uploadForm = $("#file_upload")[0].files[0];

    fd.append("my_file", uploadForm);
    //console.log(uploadForm);
    console.log(uploadForm.name);
    // Post file to server, related files: EbookLib.py, Upload.py
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
            setTimeout(function() {
                getListing();
            }, 100);

        }
    });

});

$('body').on('click', '.remove', function(e) {
    e.preventDefault();
    //alert(2);
    var rmid = $(this).context.id;
    console.dir(rmid);

    var fd = new FormData();
    fd.append("id", rmid);

    $.ajax({
        url: "remove",
        type: "POST",
        data: {id: rmid},
        contenType: "application/json; charset=utf-8",
        success: function() {
            setTimeout(function() {
                getListing();
            }, 500);
        }
    });
});

$("#scan").click(function() {
    var testpath = $("#path").val()
    $.ajax({
        url: "scan",
        type: "GET",
        data: {path: testpath},
        contentType: "application/json; charset=utf-8",
        success: function() {
            setTimeout(function() {
                getListing();
            }, 500);
        }
    });
});

/*$("#save").click(function() {
    var bookData = jsonObj.book;

    var ISBN = bookData.identifier;
    var ext = bookData.ext;
    var date = bookData.date;
    var imgext = bookData.imgext;
    fname = jsonObj.filename;


    var fd = new FormData(document.querySelector("#confirm"));
    fd.append("ISBN", ISBN);
    fd.append("ext", ext);
    fd.append("date", date);
    fd.append("fname", fname);
    fd.append("imgext", imgext);


    console.log(fd.title);
    console.log(fname);

    $.ajax({
        url: "edit",
        type: "POST",
        data: fd,
        processData: false,
        contentType: false
    });

    setTimeout(function() {
        getListing();
    }, 100);

});*/
