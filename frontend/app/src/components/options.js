import { useState } from "react";
import Webcam from "react-webcam";

export default function Options(){
    const [loc, setloc] = useState(null)
    const [name, setname] = useState('')

    const _getlocation = () => {
        navigator.geolocation.getCurrentPosition(function(position) {
            setloc(position);
            console.log(position);
            _setGeolocation(position);
        });
    }

    const _registerUser = (img) => {
      var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "name": name,
        "imageurl":img
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("http://419e-163-118-242-57.ngrok.io/registeruser", requestOptions)
        .then(response => response.json())
        .then(result => {console.log(result);})
        .catch(error => console.log('error', error));
  }

    const _uploadImg = (img, action) => {
      var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "name": "John Doe",
        "img":img
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/uploadimg", requestOptions)
        .then(response => response.json())
        .then(result => {console.log(result); if(action=="register"){
          _registerUser(result.data)
        }
      })
        .catch(error => console.log('error', error));
  }

    const _setGeolocation = (location) => {
        console.log(location.coords)
        var myHeaders = new Headers();
        myHeaders.append("Content-Type", "application/json");

        var raw = JSON.stringify({
        "name": name,
        "location":{"latitude":location.coords.latitude, "longitude":location.coords.longitude}
        });

        var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
        };

        fetch("http://127.0.0.1:5000/loguser", requestOptions)
        .then(response => response.json())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
    }
    return(
        <div class="card w-120 bg-base-100 shadow-xl self-center">
        <Webcam screenshotFormat="image/jpeg" mirrored>{({ getScreenshot }) => (
          <div>
            <div class="form-control w-full max-w-xl p-4">
  <input value={name} onChange={(e)=>setname(e.target.value)} type="text" placeholder="Enter your name" class="input w-full max-w-2xl"/>
</div>
      <button
      className="btn btn-primary btn-xl m-30 w-full"
        onClick={() => {
          const imageSrc = getScreenshot()
          console.log(imageSrc)
          _uploadImg(imageSrc)
          _getlocation()

        }}
      >
        Log my location
      </button>
      <div class="divider">OR</div>
    
        <button className="btn btn-primary btn-xl m-30 w-full" onClick={() => {
          const imageSrc = getScreenshot()
          console.log(imageSrc)
          let url;
          _uploadImg(imageSrc, "register")

        }} >Register</button>
      </div>
    )}</Webcam>
        </div>
    )
}