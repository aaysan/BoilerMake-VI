function checkForNewData() {
    const getData = async () => {
      const data = await http.get({
        url: "https://webhooks.mongodb-stitch.com/api/client/v2.0/app/our_last_hackson-sfrvf/service/Capture_face/incoming_webhook/fetch_face"
      });
      console.log(data);
      // Check if there is a new value
      // Handle any new values appropriately
      checkForNewData();
    }
    setTimeout(getData, 5000)
  }