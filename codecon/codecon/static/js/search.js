$("#query").keyup(function(){
  $.ajax({
     type: "GET",
     url: '/search/results/',
     data: {
       "query" : $("#query").val()
     },
     dataType : 'html',
     success: get_results
  });
})

function results(){
  $.ajax({
     type: "GET",
     url: '/search/results/',
     data: {
       "query" : $("#query").val()
     },
     dataType : 'html',
     success: get_results
  });
}

function get_results(data, textStatus, jqXHR){
  $("#search_results").html(data)
}

results();

