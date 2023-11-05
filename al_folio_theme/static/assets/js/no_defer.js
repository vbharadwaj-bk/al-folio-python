// add bootstrap classes to tables
$(document).ready(function() {
  $('table').each(function() {
    if (document.documentElement.getAttribute("data-theme") == "dark") {
      $(this).addClass('table-dark');
    } else {
      $(this).removeClass('table-dark');
    }

    // only select tables that are not inside an element with "news" (about page) or "card" (cv page) class
    if($(this).parents('[class*="news"]').length==0 &&
        $(this).parents('[class*="card"]').length==0 &&
        $(this).parents('code').length == 0) {
      // make table use bootstrap-table
      $(this).attr('data-toggle','table');
      $(this).attr('data-classes','table table-sm');
      // add some classes to make the table look better
      $(this).addClass('table-hover');
    }
  })
});

