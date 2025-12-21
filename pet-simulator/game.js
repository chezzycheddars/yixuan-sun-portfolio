function updatePet() {
  var petType = $("select#pet-type").val();
  $("#pet").attr("src", `images/${petType}-sitting.png`);
  
  makeSound(petType);
  
  return petType;
}
function feedPet() {
  var petType = updatePet();
  $("#pet").attr("src", `images/${petType}-eating.png`);
}

function makeSound(petType) {
  var bark = new Audio("audio/bark.wav");
  var meow = new Audio("audio/meow.wav");
  
  if (petType == "dog") {
      bark.play()
  } else {
      meow.play()
  }
}

function changeBackground() {
  var background = $("select#background").val();
  $("#game").css("background-image", `url('images/${background}.jpg')`);
}
function walkPet() {
  function resetPet() {
    $("#pet").css("left", "-500px")
    $("#pet").animate({"left": "50%"});
  }
  var petType = updatePet();
  var petX = $("#pet").position.left;
  console.log(petX)
  $("#pet").attr("src", `images/${petType}-standing.png`);
  $("#pet").animate({"left": "800px"});
  setTimeout(resetPet, 2000);
}

$("#pet-type").click(updatePet);
$("#feed").click(feedPet);
$("#background").click(changeBackground);
$("#walk").click(walkPet);

function saveStats() {
  var user = $('user').text();
  var userStats = JSON.stringify(userStatsObj);
  localStorage.setItem(user, userStats);
}

function updateStats() {
  var user = $("#user").text();
  
  if (user == ""){
    return;
  }
  
  saveStats();
  
  var userAccount = localStorage.getItem(user);
  userStatsObj = JSON.parse(userAccount);
  
  $("#health > div").text(userStatsObj.health);
  $("#happiness > div").text(userStatsObj.happiness);
  $("#hunger > div").text(userStatsObj.hunger);
}

var userStatsObj;
userStatsObj.health -= 1;
userStatsObj.hunger += 1;
userStatsObj.happiness -= 1;

setInterval(updateStats, 1000);

