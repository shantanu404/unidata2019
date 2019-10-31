function get_content(name, inst, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(xhr.responseText);
    }
  }

  xhr.open('GET', '/api/' + name + '/' + inst);
  xhr.send();
}

function main() {
  var btn = document.getElementById('submit_btn')
  .addEventListener('click', function(e) {
    e.preventDefault();
    var name = document.getElementById('name_input')
                .value.replace(/\s/gi, '_');
    var menu = document.getElementById('tgt_inst_input');
    var inst = menu.options[menu.selectedIndex].text.toLowerCase();

    get_content(name, inst, function(data) {
      console.log(data);
    });
  });
}

window.addEventListener('DOMContentLoaded', main)