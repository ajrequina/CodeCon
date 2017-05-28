console.log("HEY HEY")
$.ajax({
     type: "GET",
     url: '/notifications/',
     data: "check",
     success: function(response){

         data = JSON.parse(response.notifications)
         console.log(data)
         $("#notifications").append('<li><a href="/user/messages"><span class="tab">Message Center</span></a></li>');
     }
});