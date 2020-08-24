$(function () {
    $("#contactform").submit(function (e){
	e.preventDefault();

	var form = $(this);
	var url = form.attr("action");
	var name = $("#name").val();
	var email = $("#email").val();
	var message = $("#message").val();

	$.ajax({
	    type: "POST",
	    url: url,
	    data: {
		name: name,
		email: email,
		message: message,
	    },
	    success: function (data) {
		$("#response").html("Message sent!")
	    },
	    failure: function(data) {
		$("#response").html("Message failed!")
	    }
	});

    });
});
