$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-location .modal-content").html("");
          $("#modal-location").modal("show");
        },
        success: function (data) {
          $("#modal-location .modal-content").html(data.html_form);
        }
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#location-table tbody").html(data.html_location_list);
            $("#modal-location").modal("hide");
          }
          else {
            $("#modal-location .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
  
  
    /* Binding */
  
    // Create location
    $(".js-create-location").click(loadForm);
    $("#modal-location").on("submit", ".js-location-create-form", saveForm);
  
    // Update location
    $("#location-table").on("click", ".js-update-location", loadForm);
    $("#modal-location").on("submit", ".js-location-update-form", saveForm);
  
    // Delete location
    $("#location-table").on("click", ".js-delete-location", loadForm);
    $("#modal-location").on("submit", ".js-location-delete-form", saveForm);
  
  });
  