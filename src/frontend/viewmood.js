(function() {
    "use strict";
    window.addEventListener("load", init);
  
    function init() {
        getMoods();
    }
  
    function getMoods() {
        getFromURL("http://127.0.0.1:5000/get_word_assoc/");
    }

    function populateMoods(resp) {
        document.getElementById("bigMad").innerHTML = resp[3];
        document.getElementById("smallMad").innerHTML = resp[2];
        document.getElementById("smallHappy").innerHTML = resp[1];
        document.getElementById("bigHappy").innerHTML = resp[0];
    }
  
    function getFromURL(url) {
      var settings = {
        "async": true,
        "crossDomain": true,
        "url": url,
        "method": "GET",
        "headers": {
          "cache-control": "no-cache",
          "Postman-Token": "eb9966bc-d1fb-4af9-81c2-10b0222dbe1a"
        }
      }
      
      $.ajax(settings).done(function (response) {
        console.log(response);
        populateMoods(response);
      });
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
  