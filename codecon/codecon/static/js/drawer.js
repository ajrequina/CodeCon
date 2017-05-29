$(document).ready(function(){
	height = $("body").height() - $(".navbar").height() - $(".buttonSpan").height();
	$(".postPanel").css("height",  height);

	$(".postButton").click(function(){
		height = $("body").height() - $(".navbar").height() - $(".buttonSpan").height();
		// height = height - 70;
		$(".postPanel").css("height",  height);
		$(".postPanel").css("max-height",  height);
		$('.postPanel').slideToggle("slow");
		$('#userPanel').slideToggle("slow");
		if ($(".postButton").text() == "HIDE PUBLISHER"){
    	    $(".postButton").text("CREATE CONTENT");
	    } else {
	        $(".postButton").text("HIDE PUBLISHER");
	        $(".postPanel").css("display", "flex");
	    }
	});
});