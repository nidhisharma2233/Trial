let card = document.querySelector(".trend");
let card2 = document.getElementById("trendsec");
let abouts = document.querySelector(".about");
let contact = document.querySelector(".contact");
let conn = document.getElementById("connn");

console.log(card);
let blog = document.querySelector(".trends");


let mainPage = document.querySelector(".main");

function homes() {
  contact.style.display = "none";
  conn.style.display = "none";
  mainPage.style.display = "flex";
  blog.style.display = "block";
  card.style.display = "block";
  card2.style.display = "block";
  abouts.style.display = "none";

  document.getElementById("blog").style.color = "black";
  document.getElementById("home").style.color = "blue";
  document.getElementById("shop").style.color = "black";
  document.getElementById("aboutss").style.color = "black";
  document.getElementById("contact").style.color = "black";


}

function shops() {
  contact.style.display = "none";
  conn.style.display = "none";
  mainPage.style.display = "none";
  blog.style.display = "none";
  card.style.display = "block"
  card2.style.display = "block";
  abouts.style.display = "none";

  document.getElementById("blog").style.color = "black";
  document.getElementById("home").style.color = "black";
  document.getElementById("shop").style.color = "blue";
  document.getElementById("aboutss").style.color = "black";
  document.getElementById("contact").style.color = "black";

}


function blogs() {
  contact.style.display = "none";
  conn.style.display = "none";
  mainPage.style.display = "none";
  card.style.display = "none";
  card2.style.display = "none";
  blog.style.display = "block";
  abouts.style.display = "none";

  document.getElementById("blog").style.color = "blue";
  document.getElementById("home").style.color = "black";
  document.getElementById("shop").style.color = "black";
  document.getElementById("aboutss").style.color = "black";
  document.getElementById("contact").style.color = "black";

}

function about() {
  mainPage.style.display = "none";
  card.style.display = "none";
  card2.style.display = "none";
  blog.style.display = "none";
  abouts.style.display = "block";
  contact.style.display = "none";
  conn.style.display = "none";


  document.getElementById("blog").style.color = "black";
  document.getElementById("home").style.color = "black";
  document.getElementById("shop").style.color = "black";
  document.getElementById("aboutss").style.color = "blue";
  document.getElementById("contact").style.color = "black";




}
function cotacts() {
  mainPage.style.display = "none";
  card.style.display = "none";
  card2.style.display = "none";
  blog.style.display = "none";
  abouts.style.display = "none";
  contact.style.display = "block";
  conn.style.display = "block";



  document.getElementById("blog").style.color = "black";
  document.getElementById("home").style.color = "black";
  document.getElementById("shop").style.color = "black";
  document.getElementById("aboutss").style.color = "black";
  document.getElementById("contact").style.color = "blue";

}

