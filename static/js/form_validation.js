// Only Accepting alphabets & space
$.validator.addMethod("onlyLetters", function(value, element) {
  return this.optional(element) || /^^[a-zA-Z][A-Za-z\s]*$/.test(value);
}, "This field contains only alphabets");

$.validator.addMethod("emailRule", function (value, element) {
    return this.optional(element) || /[A-Za-z0-9_.-]+@[A-Za-z0-9-]+\.[a-zA-Z]+/.test(value);
}, "Please enter a valid email address.");

$.validator.addMethod("atLeastOneUppercaseLetter", function (value, element) {
    return this.optional(element) || /[A-Z]+/.test(value);
}, "Please enter valid password");

$.validator.addMethod("atLeastOneNumber", function (value, element) {
    return this.optional(element) || /[0-9]+/.test(value);
}, "Please enter valid password");

$.validator.addMethod("atLeastOneSymbol", function (value, element) {
    return this.optional(element) || /[!@#$%^&*()_./]+/.test(value);
}, "Please enter valid password");


$("#SignUpForm").validate({
  rules: {
      first_name: {
        required: {
          depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        onlyLetters:true
      },
      last_name: {
        required: {
          depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        onlyLetters:true
      },
      zipcode: {
        minlength:5,
        maxlength: 5,
      },
      email: {
        required: {
          depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        emailRule:true,
      },
      password: {
        atLeastOneUppercaseLetter:true,
        atLeastOneNumber: true,
        atLeastOneSymbol : true
      },
      confirm_password: {
        atLeastOneUppercaseLetter:true,
        atLeastOneNumber: true,
        atLeastOneSymbol : true,
        equalTo : "#password"
      }
    },
  messages: {
      first_name: {
        onlyLetters:"First Name contains only alphabets"
      },
      last_name: {
        onlyLetters:"Last Name contains only alphabets"
      },
      zipcode: {
        minlength:"Zipcode should be of 5 digits",
        maxlength:"Zipcode should be of 5 digits"
      },
      confirm_password: {
        equalTo : "Password & confirm password does'nt match"
      }
    },
});



$("#LoginForm").validate({
  rules: {
      user_email: {
        required: {
          depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        emailRule:true
      },
      user_password : {
      required: {
        depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        atLeastOneUppercaseLetter:true,
        atLeastOneNumber: true,
        atLeastOneSymbol : true
      }
    },
    messages: {
      user_password: {
        atLeastOneUppercaseLetter:"Seems invalid password",
        atLeastOneNumber:"Seems invalid password",
        atLeastOneSymbol:"Seems invalid password"
      }
    },
  });


$("#ForgetForm").validate({
  rules: {
      forget_email: {
        required: {
          depends:function(){
            $(this).val($.trim($(this).val()));
            return true;
        }
        },
        emailRule:true,
      }
    }  
});


$("#DealSearchForm").validate({
  rules: {
      zip_code: {
        required: true,
        number: true
      },
      service_category_id : {
        required: false
      }
    },
  messages : {
     zip_code: {
        number: "Please enter numbers only"
      },
  }  
  });


$("#ContactUsForm").validate({
  rules: {
      contact_name: {
        required: true,
        onlyLetters : true
      },
      contact_email : {
        required: true,
        emailRule: true
      },
      contact_subject : {
        normalizer: function(value) {
        return $.trim(value);
      }
      },
      contact_message : {
        normalizer: function(value) {
        return $.trim(value);
      }
      }
    }  
  });

  // confirm password
$("#resetpasswordForm").validate({
  rules: {
      reset_password: {
      atLeastOneUppercaseLetter:true,
      atLeastOneNumber: true,
      atLeastOneSymbol : true
    },
    reset_confirm_password: {
      atLeastOneUppercaseLetter:true,
      atLeastOneNumber: true,
      atLeastOneSymbol : true,
      equalTo : "#new_password"
    }

  },
  messages: {
      reset_confirm_password: {
      equalTo : "Password & confirm password does'nt match"
    }

  }
});


$("#home_searchzip_code").validate({
  rules: {
      zip_code: {
        required: true,
        number: true
      }
    },
  messages : {
     zip_code: {
        number: "Please enter numbers only"
      },
  }  
  });

$("#footer_searchzip_code").validate({
  rules: {
      zip_code: {
        required: true,
        number: true
      }
    },
  messages : {
     zip_code: {
        number: "Please enter numbers only"
      },
  }  
  });