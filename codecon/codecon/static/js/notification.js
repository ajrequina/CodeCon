var data = []
function get_notifs(){

    $.ajax({
       type: "GET",
       url: '/notifs/unread/',
       data: "check",
       success: function(response){
        var temp = JSON.parse(response.notifs)

        for(var i = 0; i < temp.length; i++){
          var found = false;
          for(var j = 0; j < data.length; j++){
            if(temp[i].pk == data[j].pk){
              found = true;
              break;
            }
          }

          if(found == false){
            data.unshift(temp[i])
            console.log(data.length)
            $("#notifs-count").text(data.length)
            var li = $("<li></li>")
            var a = $('<a>')
            a.click(function(event) {
              event.preventDefault();
              var pk = $(this).attr("id");
              var link = $(this).attr("href");
              $.ajax({
                type: "GET",
                url: '/notifs/mark_as_read/' + pk + "/",
                data: "check",
                success : function(data){
                  if(data.is_marked){
                    window.location.href = link;
                  }
                }
              })
            }).end();

            li.append(a)
            var type = temp[i].fields.page_type;
            if(type == "post"){
               a.attr('href', '/post/detail/' + temp[i].fields.target_pk + "/")
            }

            var date = new Date(temp[i].fields.create_date)
            a.text(temp[i].fields.description + " " + jQuery.timeago(date))
            a.attr('id', temp[i].pk)
            $("#notifs").prepend(li)
            $("#notifs li:lt(5)").slice(0, 5).show();
            

          }
        }
      } 
  });
}

setInterval(get_notifs, 1000)
