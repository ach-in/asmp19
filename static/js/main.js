$(document).ready(function(){
  $(".menu-button, #overlay li").click(function(){
  $(".menu-button").toggleClass('active');
  $('#overlay').toggleClass('open');
  if($(document.body).hasClass("menu-open"))
    $(document.body).removeClass("menu-open");
  else
    $(document.body).addClass("menu-open");
  });
   $(window).scroll(function(){
          if($(this).scrollTop() > 100){
              $('#scroll').fadeIn();
          }else{
              $('#scroll').fadeOut();
          }
      });
      $('#scroll').click(function(){
          $("html, body").animate({ scrollTop: 0 }, 600);
          return false;
      });
  $("a").on('click', function(event) {
    if (this.hash !== "") {
      event.preventDefault();
      var hash = this.hash;
      $('html, body').animate({
        scrollTop: $(hash).offset().top
      }, 800, function(){
        window.location.hash = hash;
      });
    }
  });
});

