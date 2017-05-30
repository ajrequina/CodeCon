$("#show-followers").click(function(event){
  event.preventDefault()
  link = $(this).attr('href');
  $.ajax({
     type: "GET",
     url: link,
     data: "",
     dataType : 'html',
     success: get_followers
  });
})

function get_followers(data, textStatus, jqXHR){
  $("#followers-list").html(data)
}

$("#show-following").click(function(event){
  event.preventDefault()
  link = $(this).attr('href');
  $.ajax({
     type: "GET",
     url: link,
     data: "",
     dataType : 'html',
     success: get_following
  });
})

function get_following(data, textStatus, jqXHR){
  $("#following-list").html(data)
}
