function showModal(name,desc,url, loc,cat){
    $("#img-label").text(name)
    $("#myModal").modal("show")
    $(".modal-title").text(name)
    
    $("#img-likes").text(desc)
    $("#img-pub_date").text("Location: " + loc)
    $("#img-comments").text("Category: " + cat)
   
}
/* <p id="img-likes"></p>>
<p id="img-pub_date"></p>
<p id="img-comments"></p>
<p id="img-likes"></p> */