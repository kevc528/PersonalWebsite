function loadNav() {
  $("#nav-placeholder").load("nav.html");
}

function loadFooter() {
  $("#footer-placeholder").load("footer.html");
}

function downloadResume() {
  window.open('resume.pdf');
}

function innerLoadNav() {
  $("#nav-placeholder").load("../nav.html");
  $("#home-link").attr("href", "../");
  $("#projects-link").attr("href", "../projects");
  $("#contact-link").attr("href", "../contact");
  $("#download-button").attr("onclick", "innerDownloadResume()");
}

function innerLoadFooter() {
  $("#footer-placeholder").load("../footer.html");
}

function innerDownloadResume() {
  window.open('../resume.pdf');
}