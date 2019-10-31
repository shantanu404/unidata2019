function main() {
  var btn = document.getElementById('submit_btn');
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    console.log('Clicked!');
  });
}

window.addEventListener('DOMContentLoaded', main)