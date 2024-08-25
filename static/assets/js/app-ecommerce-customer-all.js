/**
 * App eCommerce customer all
 */

'use strict';

// Datatable (jquery)
//  validation on visa_type 
(function () {
  const phoneMaskList = document.querySelectorAll('.phone-mask'),
  visa_type_form = document.getElementById('visa_type_form');

  
  // Add New customer Form Validation
  const fv = FormValidation.formValidation(visa_type_form, {
    fields: {
      name: {
        validators: {
          notEmpty: {
            message: 'Please enter fullname '
          }
        }
      },
     
    },
  });
})();
