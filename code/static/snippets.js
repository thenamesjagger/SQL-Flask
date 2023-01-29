function filterSnippets() {
  let input = document.getElementById("filter-input").value.toLowerCase();
  let snippetCards = document.getElementsByClassName("snippet-card");

  for (let i = 0; i < snippetCards.length; i++) {
      let snippetCard = snippetCards[i];
      let description = snippetCard.getElementsByClassName("description")[0].innerHTML;
      if (description.toLowerCase().indexOf(input) > -1) {
          snippetCard.style.display = "block";
      } else {
          snippetCard.style.display = "none";
      }
  }
}

function deleteSnippet(id) {
    let request = new XMLHttpRequest();
    request.open("DELETE", `/snippet/${id}`);
    request.onload = function() {
      // If the deletion was successful, remove the snippet from the page
      if (request.status === 200) {
        let snippetCard = document.querySelector(`.snippet-card h2:contains('Code Snippet ${id}')`).parentNode;
        snippetCard.parentNode.removeChild(snippetCard);
      }
    };
    request.send();
    location.reload();
  }
  