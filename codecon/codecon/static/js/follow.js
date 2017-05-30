$("#show-followers").click(function(event){
  event.preventDefault()
  link = $(this).attr('href');
  $.ajax({
     type: "GET",
     url: link,
     data: "",
     dataType : 'html',
     success: get_results
  });
})

$("#show-following").click(function(event){
  event.preventDefault()
  link = $(this).attr('href');
  $.ajax({
     type: "GET",
     url: link,
     data: "",
     dataType : 'html',
     success: get_results
  });
})

function get_results(data, textStatus, jqXHR){
  $("#follow-list").html(data)
}
