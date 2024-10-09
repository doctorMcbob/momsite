$(function () {
    $("#contactform").submit(function (e){
	e.preventDefault();
	grecaptcha.ready(function() {
            grecaptcha.execute('6LdJMg4pAAAAAIK9sw94AMXp89Hs43nfT_IT6T4L', {action: 'submit'}).then(function(token) {
		var form = $(this);
		var url = "/email";
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
			token: token,
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
    });
});
