function submit(eventObj) {
  eventObj.preventDefault();
  var name = $("#name").val();
  var email = $("#email").val();
  var feedback = $("#feedback").val();
  
  if (name == "" || email == "" || feedback == "") {
      window.alert("You left one or more of the textboxes empty. Please fill out all textboxes to submit.");
      return;
  };

  $("#login").hide();
  $("#thank-you").show();
  var userFeedback = `
  <p>${name} </p>
  <p>${email} </p>
  <p>${feedback}</p> 
  `;

  $("#thank-you").append(userFeedback);
}


$("#submit-btn").click(submit);
$("#thank-you").hide();
