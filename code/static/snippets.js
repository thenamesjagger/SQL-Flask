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