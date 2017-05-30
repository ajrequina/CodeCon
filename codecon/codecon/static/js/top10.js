console.log("I am here")
function get_top10(){
    $.ajax({
       type: "GET",
       url: '/post/top10/',
       data: "check",
       dataType : 'html',
       success: append_top10
  });
}


function append_top10(data, textStatus, jqXHR){
  $("#top10-list").html(data)
}

get_top10()
setInterval(get_top10, 5000)
