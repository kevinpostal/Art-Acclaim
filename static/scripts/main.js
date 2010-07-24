// Search Dropdown Box

$(document).ready(function(){$('.search_link').hoverIntent(function() {$('.search_select').slideDown('slow');return false;},function() {})});
$(document).ready(function(){$('.search_type').click(function() {$('.search_select').slideUp('fast');return false;})});

$(document).ready(function(){$('.right_column').hover(function() {$('.search_select').hide();return false;})});
$(document).ready(function(){$('.main_tab').hover(function() {$('.search_select').hide();return false;})});
$(document).ready(function(){$('.search_text').hover(function() {$('.search_select').hide();return false;})});



// Search Dropdown Select

$(document).ready(function(){$('#select_people').click(function() {$('#active_title').hide();return false;})});
$(document).ready(function(){$('#select_people').click(function() {$('#active_tags').hide();return false;})});
$(document).ready(function(){$('#select_people').click(function() {$('#active_topics').hide();return false;})});

$(document).ready(function(){$('#select_people').click(function() {$('#active_people').fadeIn('slow');return false;})});


$(document).ready(function(){$('#select_tags').click(function() {$('#active_title').hide();return false;})});
$(document).ready(function(){$('#select_tags').click(function() {$('#active_people').hide();return false;})});
$(document).ready(function(){$('#select_tags').click(function() {$('#active_topics').hide();return false;})});

$(document).ready(function(){$('#select_tags').click(function() {$('#active_tags').fadeIn('slow');return false;})});


$(document).ready(function(){$('#select_topics').click(function() {$('#active_title').hide();return false;})});
$(document).ready(function(){$('#select_topics').click(function() {$('#active_people').hide();return false;})});
$(document).ready(function(){$('#select_topics').click(function() {$('#active_tags').hide();return false;})});

$(document).ready(function(){$('#select_topics').click(function() {$('#active_topics').fadeIn('slow');return false;})});



// Link Animation

(function($) {
	$.extend($.fx.step,{
	    backgroundPosition: function(fx) {
            if (fx.state === 0 && typeof fx.end == 'string') {
                var start = $.curCSS(fx.elem,'backgroundPosition');
                start = toArray(start);
                fx.start = [start[0],start[2]];
                var end = toArray(fx.end);
                fx.end = [end[0],end[2]];
                fx.unit = [end[1],end[3]];
			}
            var nowPosX = [];
            nowPosX[0] = ((fx.end[0] - fx.start[0]) * fx.pos) + fx.start[0] + fx.unit[0];
            nowPosX[1] = ((fx.end[1] - fx.start[1]) * fx.pos) + fx.start[1] + fx.unit[1];
            fx.elem.style.backgroundPosition = nowPosX[0]+' '+nowPosX[1];

           function toArray(strg){
               strg = strg.replace(/left|top/g,'0px');
               strg = strg.replace(/right|bottom/g,'100%');
               strg = strg.replace(/([0-9\.]+)(\s|\)|$)/g,"$1px$2");
               var res = strg.match(/(-?[0-9\.]+)(px|\%|em|pt)\s(-?[0-9\.]+)(px|\%|em|pt)/);
               return [parseFloat(res[1],10),res[2],parseFloat(res[3],10),res[4]];
           }
        }
	});
})(jQuery);

$(function(){$('.top_navigation a')
	.css( {backgroundPosition: "100% 100%"} )
	.mouseover(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 75%)"}, 
			{duration:100})
		})
	.mouseout(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 100%)"}, 
			{duration:100})
		})})


$(function(){$('.search_form a')
	.css( {backgroundPosition: "100% 100%"} )
	.mouseover(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 75%)"}, 
			{duration:100})
		})
	.mouseout(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 100%)"}, 
			{duration:100})
		})})
		
		
$(function(){$('.main_tab_container a')
	.css( {backgroundPosition: "100% 70%"} )
	.mouseover(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 100%)"}, 
			{duration:100})
		})
	.mouseout(function(){
		$(this).stop().animate(
			{backgroundPosition:"(100% 70%)"}, 
			{duration:100})
		})})	
		
		
		
// Clear Form 

$(document).ready(function(){$(".search_text").focus(function() {if ( $(this).val() == "Search")$(this).val('')})});
$(document).ready(function(){$(".search_text").blur(function() {if ( $(this).val() == "")$(this).val('Search')})});	


//JQuery Fade Toggle


//$(document).ready(function(){$('.search_link').click(function(){$('.search_select').fadeIn('50')})});

//$(document).ready(function(){$('.search_select').mouseout(function(){$('.search_select').fadeOut('50')})});




// Help Menu

$(document).ready(function() {

$("#help_menu_id > li > a.expanded + ul").slideToggle("medium");
	$("#help_menu_id > li > a").click(function() {
	$(this).toggleClass("expanded").toggleClass("collapsed").find("+ ul").slideToggle("medium");
	});});



// Gallery Color Box

$(document).ready(function(){$("a[rel='art_colorbox']").colorbox()});


// Fancy Box

$(document).ready(function() {
	$(".friend_close_button").fancybox({
		'titlePosition'		: 'outside',
		'autoScale'			: true,
		'transitionIn'		: 'fade',
		'transitionOut'		: 'fade'
		
		});
		
	});