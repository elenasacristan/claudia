window.onload = () => {
    typeWriter();
};
  
var i = 0;
var txt =
  "My passion is online marketing, Why don’t we do something together?"; /* The text */
var speed = 50; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
  if (i < txt.length) {
    document.getElementById("type-sentence").innerHTML += txt.charAt(i);
    i++;
    setTimeout(typeWriter, speed);
  }
}
