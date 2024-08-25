/**
 *  Pages Authentication
 */

'use strict';
const formAuthentications = document.querySelectorAll('.formAuthentication');

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    // Form validation for Add new record
      formAuthentications.forEach(formAuthentication=>{
        
        FormValidation.formValidation(formAuthentication, {
          fields: {
          
            email: {
              validators: {
                notEmpty: {
                  message: 'Please enter your email'
                },
                emailAddress: {
                  message: 'Please enter valid email address'
                }
              }
            },
           
            password: {
              validators: {
                notEmpty: {
                  message: 'Please enter your password'
                },
                stringLength: {
                  min: 8,
                  message: 'Password must be more than 8 characters'
                }
              }
            },
            'confirm_password': {
              validators: {
                notEmpty: {
                  message: 'Please confirm password'
                },
                identical: {
                  compare: function () {
                    return formAuthentication.querySelector('[name="password"]').value;
                  },
                  message: 'The password and its confirm are not the same'
                },
                stringLength: {
                  min: 8,
                  message: 'Password must be more than 8 characters'
                }
              }
            },
            terms: {
              validators: {
                notEmpty: {
                  message: 'Please agree terms & conditions'
                }
              }
            }
          },
          plugins: {
            trigger: new FormValidation.plugins.Trigger(),
            bootstrap5: new FormValidation.plugins.Bootstrap5({
              eleValidClass: '',
              rowSelector: '.mb-3'
            }),
            submitButton: new FormValidation.plugins.SubmitButton(),
  
            defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
            autoFocus: new FormValidation.plugins.AutoFocus()
          },
          init: instance => {
            instance.on('plugins.message.placed', function (e) {
              if (e.element.parentElement.classList.contains('input-group')) {
                e.element.parentElement.insertAdjacentElement('afterend', e.messageElement);
              }
            });
          }
        });


      })

    //  Two Steps Verification
    const numeralMask = document.querySelectorAll('.numeral-mask');

    // Verification masking
    if (numeralMask.length) {
      numeralMask.forEach(e => {
        new Cleave(e, {
          numeral: true
        });
      });
    }
  })();
});
