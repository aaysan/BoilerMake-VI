//var http = require('http');
function checkForNewData() {
    console.log("data");
    const getData = async () => {
    console.log("data");
     const data = await fetch(
        "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/Capture_face/incoming_webhook/fetch_face"
    ).then(function(response) {
        return response.json();
    });
     console.log(JSON.stringify(data));
      // Check if there is a new value
      // Handle any new values appropriately
      checkForNewData();
    }
    setTimeout(getData, 5000)
  }
