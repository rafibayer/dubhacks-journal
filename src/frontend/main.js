(function() {
  "use strict";

  window.addEventListener("load", init);

  function init() {
    id("signup").addEventListener("click", signup);
    //id("login").addEventListener("click", login);
    id("login").addEventListener("click", testAPI);
    addPageInd();
  }

  function signup() {
    window.open("signup.html","_self")
  }

  function getEmotionFromCamera() {
    result = getFromURL("http://127.0.0.1:5000/take_picture/");
    alert(result);
  }

  function login() {
    window.open("login.html","_self")
  }



  function addPageInd() { //add function to make the indicator change when scrolling!!
    id("dashboard").addEventListener("click", activeDash);
    id("about").addEventListener("click", activeAbout);
    id("contact").addEventListener("click", activeContact);
  }

  function activeDash() {
    removeInd();
    id("dashboard").classList.add("selected");
  }

  function activeAbout() {
    removeInd();
    id("about").classList.add("selected");
  }

  function activeContact() {
    removeInd();
    id("contact").classList.add("selected");
  }

  function removeInd() {
    id("dashboard").classList.remove("selected");
    id("about").classList.remove("selected");
    id("contact").classList.remove("selected");
  }

  function getFromURL(url) {
    fetch(url)
      .then(checkStatus)
      .then(returnPromise);
  }

  function returnPromise(responce) {
    return responce;
  }

  /**
  function getFromURL(url) {
    fetch(url)
      .then(checkStatus)
      .then(getText)
      .catch(console.log);
  }

  function getText(string) {

  }
  */

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
