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

    var loadDepartmentForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-department .modal-content").html("");
          $("#modal-department").modal("show");
        },
        success: function (data) {
          $("#modal-department .modal-content").html(data.html_form);
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
  
    var saveDepartmentForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (data) {
          if (data.form_is_valid) {
            $("#department-table tbody").html(data.html_department_list);
            $("#modal-department").modal("hide");
          }
          else {
            $("#modal-department .modal-content").html(data.html_form);
          }
        }
      });
      return false;
    };
    /* Binding */
  
    // Create location
    $(".js-create-location").click(loadForm);
    $("#modal-location").on("submit", ".js-location-create-form", saveForm);
  
    // Create department
    $(".js-create-department").click(loadDepartmentForm);
    $("#modal-department").on("submit", ".js-department-create-form", saveDepartmentForm);

    // Update location
    $("#location-table").on("click", ".js-update-location", loadForm);
    $("#modal-location").on("submit", ".js-location-update-form", saveForm);

    // Update department
    $("#department-table").on("click", ".js-update-department", loadDepartmentForm);
    $("#modal-department").on("submit", ".js-department-update-form", saveDepartmentForm);
  
    // Delete location
    $("#location-table").on("click", ".js-delete-location", loadForm);
    $("#modal-location").on("submit", ".js-location-delete-form", saveForm);

    // Delete department
    $("#department-table").on("click", ".js-delete-department", loadDepartmentForm);
    $("#modal-department").on("submit", ".js-department-delete-form", saveDepartmentForm);
  
  });
  