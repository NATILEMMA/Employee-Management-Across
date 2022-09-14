document.querySelector("#fill_attendance").addEventListener("submit", function(e){
		if(!isValid){
			e.preventDefault();
    //stop form from submitting
		}
		  //do whatever an submit the form

		  consol.log("hello this is my name");
	});





var employeeDash.call = function (args, callback) {
	employeeDash.set_status('{{ _("Verifying...") }}', 'blue');

	return frappe.call({
		type: "POST",
		args: args,
		callback: callback,
		freeze: true,
		statusCode: employeeDash.employeeDash_handlers
	});
}

frappe.ready(function () {

	employeeDash.bind_events();


	$(".form-signup, .form-forgot").removeClass("hide");
});


