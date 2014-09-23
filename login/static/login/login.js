function testInput(id) {
  switch(id) {
    case "#regUmail":
      return /(@umail.ucsb.edu)$/.test($(id).val());
    case "#regPassword":
      return /^[a-zA-Z0-9].{4,14}$/.test($(id).val());
    case "#finalPassword":
      return ($(id).val() === $("#regPassword").val());
    case "#userName":
      return /^[a-zA-Z0-9].{4,14}$/.test($(id).val());
  }
}

$(document).ready(function() {
  //add tooltips
	$("[data-toggle='tooltip']").tooltip();

  $("#loginForm").submit(function(event){
    //prevent submit
    event.preventDefault();

    //remove errors
    $("#forUmail").removeClass("has-error");
    $("#forPass").removeClass("has-error");

    //get form input
    umail = $("#inputUmail").val();
    password = $("#inputPassword").val();
    
    if(umail === "") //no umail
      $("#forUmail").addClass("has-error");

    if(password === "") //no password
      $("#forPass").addClass("has-error");

    if(umail != "" && password != "") //umail and password filled in
    {
      $.post("login/", $("#loginForm").serialize()); 
        /*function(data) {
          if(data.fail === "fail")
          {
            if(data.umail != "") //valid umail
            {
              console.log(data.umail);
              console.log(data.password);
              console.log(password);
              if(password != data.password)
                $("#forPass").addClass("has-error");
            }
            else //invalid umail
            {
              console.log("there");
              console.log(data.umail);
              console.log(data.password);
              console.log(password);
              $("#forUmail").addClass("has-error");
              if(password != data.password)
                $("#forPass").addClass("has-error");
            }
          }
          else
          {
            console.log("success");
          }*/
        //});
    }
  });

  $("#registerForm").submit(function(event){
    //prevent submit
    event.preventDefault();

    //remove errors
    $("#forRU").removeClass("has-error");
    $("#forRP").removeClass("has-error");
    $("#forRFP").removeClass("has-error");
    $("#forRUN").removeClass("has-error");

    //get form input
    umail = $("#regUmail").val();
    password = $("#regPassword").val();
    verify = $("#finalPassword").val();
    username = $("#userName").val();

    validUmail = testInput("#regUmail");
    validPassword = testInput("#regPassword");
    validFinalPassword = testInput("#finalPassword");
    validUsername = testInput("#userName");

    if(!validPassword)
      $("#forRP").addClass("has-error");

    if(!validFinalPassword)
      $("#forRFP").addClass("has-error");

    $.get("checkValue/", {'type': 'umail', 'umail': umail}, function(data) {
      if(data.taken === "no" && validUmail) //umail not taken and valid
      {
        $("#forRU").removeClass("has-error");
        $.get("checkValue/", {'type': 'username', 'userName': username}, function(newdata) {
          if(newdata.taken === "no" && validUsername) //username not taken and valid
          {
            $("#forRUN").removeClass("has-error");
            if(validPassword && validFinalPassword) //valid passwords
            {
              //insert into db
              $.post("register/", $("#registerForm").serialize());
              $('#myModal').modal('hide');
            }
          }
          else //username taken or invalid
          {
            $("#forRUN").addClass("has-error");
          }
        });
      }
      else //umail taken or invalid
      {
        $("#forRU").addClass("has-error");
        $.get("checkValue/", {'type': 'username', 'userName': username}, function(newdata) {
          if(newdata.taken === "no" && validUsername) //username not taken and valid
            $("#forRUN").removeClass("has-error");
          else //username taken or invalid
            $("#forRUN").addClass("has-error");
        });
      }
    });
  });


  $("#regUmail").keyup(function() {
    $.get("checkValue/", {'type': 'umail', 'umail': $(this).val()}, function(data) {
      if(data.taken === "no") //not taken
      {
        if(testInput("#regUmail")) //valid
          $("#forRU").removeClass("has-error");
        else //invalid
          $("#forRU").addClass("has-error");
      }
      else //taken
        $("#forRU").addClass("has-error");
    });
    
  });

  $("#regPassword").keyup(function() {
    if(!testInput("#regPassword"))
      $("#forRP").addClass("has-error");
    else
      $("#forRP").removeClass("has-error");
  });

  $("#finalPassword").keyup(function() {
    if(!testInput("#finalPassword"))
      $("#forRFP").addClass("has-error");
    else
      $("#forRFP").removeClass("has-error");
  });

  $("#userName").keyup(function() {
    $.get("checkValue/", {'type': 'username', 'userName': $(this).val()}, function(data) {
      if(data.taken === "no") //not taken
      {
        if(testInput("#userName")) //valid
          $("#forRUN").removeClass("has-error");
        else //invalid
          $("#forRUN").addClass("has-error");
      }
      else //taken
        $("#forRUN").addClass("has-error");
    });
  });
});
