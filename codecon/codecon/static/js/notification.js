var data = []
function get_notifs(){
    $.ajax({
       type: "GET",
       url: '/notifs/unread/',
       data: "",
       dataType : 'html',
       success: append_notifs
  });
}


function append_notifs(data, textStatus, jqXHR){
  $("#notifs").html(data)
}

get_notifs()
setInterval(get_notifs, 5000)
