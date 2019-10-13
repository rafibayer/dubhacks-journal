(function() {
    "use strict";
    var result;
    window.addEventListener("load", init);
  
    function init() {
      document.getElementById("recordEmotion").addEventListener("click", getEmotionFromCamera);
      document.getElementById("viewMoods").addEventListener("click", goToMoods);
      document.getElementById("addEntry").addEventListener("click", goToEntry);
      getRecommendation();
      addPageInd();
    }
  
    function goToMoods() {
      window.open("viewmood.html", "_self");
    }

    function goToEntry() {
      window.open("newentry.html", "_self");
    }

    function getEmotionFromCamera() {
      //alert("calling api...");
      getFromURL("http://127.0.0.1:5000/take_picture/", "camera");
    }

    function getRecommendation() {
      getFromURL("http://127.0.0.1:5000/get_happy_sad/", "recommend");

    }

    function populateRecommendation(resp) {
      console.log(resp);
      document.getElementById("personalized").innerHTML = resp;
    }
  
    // function login() {
    //   window.open("login.html","_self")
    // }
  
  
  
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
  /**
    async function getFromURL(url) {
      fetch(url, {mode:"no-cors"}).then(data=>{return data.text()})
      .then(res=>{alert(res)});
      
    }
    */
    
    
  
    function getFromURL(url, flag) {
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
        result = response;
        //console.log(result);
        if (flag == "recommend") {
          populateRecommendation(result);
        } else if (flag == "camera") {
          var text = "Your mood was detected as: ";
          text = text + result;
          populateRecommendation(text);
        }
      });
    } 
  
  
    function getText(string) {
      console.log(string);
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
  