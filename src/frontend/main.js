(function() {
  "use strict";

  window.addEventListener("load", init);

  function init() {
    id("signup").addEventListener("click", signup);
    //id("login").addEventListener("click", login);
    id("login").addEventListener("click", login); //SWITCH TO DIFF BUTTON
    addPageInd();
  }

  function signup() {
    window.open("signup.html","_self")
  }

/** short function to simply lines of code that require accessing the document
    with an id,
    @param {string} id is a string which represents an id
    @returns {element} returns the element of the id */
  function id(id) {
    return document.getElementById(id);
  }

/** short function to simply lines of code that require accessing the document
    with querySelectorAll,
    @param {string} selector is a string which represents the selector(s)
    @returns {element} returns the element of the selector(s) */
  function qsa(selector) {
    return document.querySelectorAll(selector);
  }
})();
