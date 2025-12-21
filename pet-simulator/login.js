function signup(eventObj) {
    eventObj.preventDefault();
    var username = $("#username").val();
    var password = $("#password").val();
    
    var userAccount = localStorage.getItem(username);
    if (userAccount) {
      window.alert(
        "That username is already in use! Please choose a different username."
      );
      return;
    }
    
    var userStatsObj = {
      password: password,
      health: 100,
      hunger: 0,
      happiness: 100,
    };
    var userStats = JSON.stringify(userStatsObj);
    localStorage.setItem(username, userStats);
    window.alert("Account successfully created for " + username + "!");
    grantAccess(username);  
  }

  function grantAccess(username) {
    $("#login").hide();
    $("#game").show();
    $("#user").text(username);
  }
  $("#game").hide();

  function login(eventObj) {
    eventObj.preventDefault();
    var username = $("#username").val();
    var password = $("#password").val();
    var userAccount = localStorage.getItem(username);
    if (userAccount) {
      var userStats = JSON.parse(userAccount);
      if (password == userStats.password) {
        grantAccess(username);
      } else {
        window.alert("Invalid password, please try again!");
      }
    } else {
      window.alert("There is no user by that username!");
    }
  }
  
  $("#signup-btn").click(signup);
  $("#login-btn").click(login);
