/**
 * Typeahead (jquery)
 */

'use strict';

$(function () {
  
 
  const names_list =  document.getElementById("employee_names_list")
  const cnic_list =  document.getElementById("employee_cnic_as_list")
  const not_sumbit_element = document.getElementById('not_sumbit')
  
  let isSubmit = true;

  if(not_sumbit_element){
    isSubmit = false
  }


  function create_typeahead(data, selector, name, is_submit=true){



    var bloodhoundBasicExample = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.whitespace,
      queryTokenizer: Bloodhound.tokenizers.whitespace,
      local: data
    });
  
    
    $(selector).typeahead(
      {
        hint: !isRtl,
        highlight: true,
        minLength: 1
      },
      {
        name: name,
        source: bloodhoundBasicExample
      }
    );
  
   if(is_submit){
    $(selector).bind('typeahead:select', function(ev, suggestion) {
  
      if (ev.target.closest('form')){
        ev.target.closest('form').submit()
      }
    });
   }
  }

  if (names_list){

    const employee_names_list = JSON.parse(names_list.textContent)
    create_typeahead(employee_names_list, ".names_typeahead", "employee_names_list", isSubmit)
  }

  if (cnic_list){
    const employee_cnic_list = JSON.parse(cnic_list.textContent)
    create_typeahead(employee_cnic_list, ".cnic_typeahead", "employee_cnic_list", isSubmit)
  }
  // visa_renewals_dates
  if(document.getElementById("visa_renewals_dates")){
    const dates_data = JSON.parse(document.getElementById("visa_renewals_dates").textContent)
    create_typeahead(dates_data, ".dates_typeahead", "dates_data", true)
  }

           
 
});



function copy_to_clip_board(element){
  const text =String(element.textContent).trim()
  toastr.options = {
    "closeButton": true,
    "progressBar": true,
    "positionClass": "toast-top-right",
    "showDuration": "300",
    "hideDuration": "1000",
    "timeOut": "5000",
    "extendedTimeOut": "1000",
    "showEasing": "swing",
    "hideEasing": "linear",
    "showMethod": "fadeIn",
    "hideMethod": "fadeOut"
  }
  navigator.clipboard.writeText(text).then(function(){
    
    toastr["success"]("Copied to Clipboard!!")

  }).catch(function(err){
    toastr["error"]("error while copyed the text")
  })
  
}   
