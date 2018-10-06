$(document).ready( function () {
  $('#myTable1').DataTable();

  $('#myTable2').DataTable({
    "ajax": "/person/json/",
    "columns": [
      {"data": "name"},
      {"data": "email"},
      {"data": "phone"},
      {"data": "gender"}
    ]
  });
});
