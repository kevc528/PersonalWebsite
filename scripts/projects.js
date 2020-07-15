function clickFilter(filter) {
  window.location.href = `./projects?filter=${(filter).trim().replace(/ /g,'%20')}`;
}

function getButtons(categories) {
  var html = ''
  for (var index in categories) {
    var category = categories[index];
    var template = 
      `<button type="button" class="btn btn-outline-primary btn-rounded btn-sm waves-effect" onclick="clickFilter(this.textContent)">
        ${category}</button>`
    html += template;
  }
  return html;
}

function loadProjects() {
  var urlParams = new URLSearchParams(window.location.search);
  var filter = urlParams.get('filter');
  if (filter != null) { filter = filter.replace(/%20/g, ' '); }
  for (var index in PROJECTS) {
    var project = PROJECTS[index];
    if (filter == null || project.categories.includes(filter)) {
      var template = 
      `<div class = "card" style = "margin-bottom:10px">
        <div class = "card-body">
          <a href = "./projects/${project.title.replace(/ /g, '-')}" style = "color:black"><h5 class= "card-title linkable">${project.title}</h5></a>
          <i class="card-text">${project.start_date} - ${project.end_date}
            <br>
          </i>
          <br>
          ${getButtons(project.categories)}
        </div>
      </div>`;
      $('#projects').append(template);
    }
  }
  if (filter != null) {
    $("#page-title").text(`${filter} Projects`);
    $("#description").remove();
    $("#projects").prepend('<a href="./projects.html">Back to all</a><br><br>');
  }
}