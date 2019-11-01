function handle_error(data) {
  var error = JSON.parse(data).error;
  var output = document.getElementById('data');
  output.innerHTML = '<div class="alert alert-danger">' + error + '</div>';
}

function get_content(name, inst, other, cutoff, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      callback(xhr.responseText);
    } else if (this.readyState == 4 && this.status == 500) {
      handle_error(xhr.responseText);
    }
  }

  console.log('GET', '/api/' + name + '/' + inst + '/' + other + '/' + cutoff);
  xhr.open('GET', '/api/' + name + '/' + inst + '/' + other + '/' + cutoff);
  xhr.send();
}

function main() {
  var btn = document.getElementById('submit_btn')
  .addEventListener('click', function(e) {
    e.preventDefault();
    var name = document.getElementById('name_input').value;

    var menu = document.getElementById('tgt_inst_input');
    var inst = menu.options[menu.selectedIndex].text.toLowerCase();

    var other_menu = document.getElementById('other_inst_input');
    var other = other_menu.options[other_menu.selectedIndex].text.toLowerCase();

    var cutoff = document.getElementById('ctf_input').value;

    get_content(name, inst, other, cutoff, function(data) {
      data = JSON.parse(data).data;
      var output = document.getElementById('data');
      output.innerHTML = '<div class="alert alert-primary" role="alert">'
                        + 'You have ' + data.length.toString()
                        + ' students who are before you @ '
                        + inst.toUpperCase() + ' but in top ' +
                        + cutoff.toString() + ' @ ' + other.toUpperCase()
                        + '</div>';
      var students = document.createElement('ul');
      students.className = 'list-group students'
      data.forEach(function(name) {
        var el = document.createElement('li');
        el.className = 'list-group-item student';
        el.innerText = name;
        output.appendChild(el);
      });
    });
  });
}

window.addEventListener('DOMContentLoaded', main)