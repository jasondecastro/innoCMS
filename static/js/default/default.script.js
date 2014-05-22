$(document).ready(function(){
	$(window).load(function(){
		$('body').fadeIn(1500);
	});
	
	$('#menu').click(function(){
		$('#user-actions').animate({ width: "300px" });
	});
	
	if($(window).width() < 1605){
		mobileMode();
	}
	
	$(window).resize(function(){
		if($(window).width() < 1605){
			mobileMode();
		}else{
			desktopMode();
		}
	});
	
	$('#header>#menu').click(function(){
		var WidthOfMain = $('#main-content').width();
		var NewWidth = WidthOfMain - 400
		
		if($('#user-actions').css("width") != "400px"){
			$('#main-content').animate({"width": NewWidth + "px"});
			$('#user-actions').animate({"width": "300px"});
		}	else{
			$('#main-content').animate({"width": "100%"});
			$('#user-actions').animate({"width": "0px"});		
		}
	});
	
	$('#user-actions>h3.register').click(function(){
		$('#user-actions>.con_register').slideDown();
		$('#user-actions>.con_login').slideUp();
	});
	$('#user-actions>h3.login').click(function(){
		$('#user-actions>.con_login').slideDown();
		$('#user-actions>.con_register').slideUp();
	});
});

function mobileMode(){
	$('#user-actions').css("width", 0)
	$('#menu').show();
}
function desktopMode(){
	$('#user-actions').css("width", "300px")
	$('#menu').hide();
}