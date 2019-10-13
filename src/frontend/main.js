(function() {
  "use strict";

  window.addEventListener("load", init);

  function init() {
    id("signup").addEventListener("click", signup);
    id("login").addEventListener("click", login);
    id("viewMoods").addEventListener("click", moods);
  }

  function signup() {
    window.open("signup.html","_self")
  }

  function login() {
    window.open("login.html","_self")
  }

  function moods() {
    window.open("viewmood.html","_self")
  }

  function getFromURL(url) {
    fetch(url)
      .then(checkStatus)
      .then(return)
      .catch(console.log);
  }

/** helper function to return the response's result text if successful, otherwise
    returns the rejected Promise result with an error status and corresponding text
    @param {object} response - response to check for success/error
    @returns {object} - valid result text if response was successful, otherwise
    rejected promise result */
  function checkStatus(response) {
    if (response.status >= 200 && response.status < 300 || response.status == 0) {
      return response.text();
    } else {
      return Promise.reject(new Error(response.status + ": " + response.statusText));
    }
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
