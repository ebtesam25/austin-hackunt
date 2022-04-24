import logo from './logo.svg';
import './App.css';
import Navbar from './components/navbar';
import Options from './components/options';
import { useEffect, useState } from 'react';

function App() {
  const _getTracks = () => {
    var requestOptions = {
      method: 'GET',
      redirect: 'follow'
    };
    
    fetch("http://419e-163-118-242-57.ngrok.io/gettracks", requestOptions)
      .then(response => response.json())
      .then(result =>{ console.log(result); settracks(result)})
      .catch(error => console.log('error', error));
  }
  const [tracks, settracks] = useState({"tracks": [{"imageurl": "https://storage.googleapis.com/hackerbucket/img.jpg", "lat": 38.8090219, "lng": -77.3233042,
    "name": "ebtesam"}, {"imageurl": "https://storage.googleapis.com/hackerbucket/img.jpg", "lat": 38.8090236, "lng":
    -77.323327, "name": "ebtesam"}, {"imageurl": "https://storage.googleapis.com/hackerbucket/img.jpg", "lat": 38.8090399,
    "lng": -77.3233152, "name": "ebtesam"}, {"imageurl": "https://storage.googleapis.com/hackerbucket/img.jpg", "lat":
    38.8090397, "lng": -77.3233176, "name": "ebtesam"}, {"imageurl": "https://storage.googleapis.com/hackerbucket/img.jpg",
    "lat": 38.8090446, "lng": -77.3233093, "name": "ebtesam"}, {"imageurl":
    "https://storage.googleapis.com/hackerbucket/img.jpg", "lat": 38.8090261, "lng": -77.3233188, "name": "ebtesam"}]})

    useEffect(() => {
      _getTracks()
    }, [])
  return (
    <div className="App">
      <header>
      <Navbar/>
      </header>
      <body className="bg-blue-900">
        <div className="grid place-items-center h-screen">
        <Options/>
        </div>

        <div id="logs">
        <div class="overflow-x-auto">
  <table class="table w-full">
    <thead>
      <tr>
        <th>Name</th>
        <th>Image</th>
        <th>Latitude</th>
        <th>Longitude</th>
      </tr>
    </thead>
    <tbody>
      {tracks.tracks.map((t)=>(<tr>
        <td>{t.name}</td>
        <td><img className="mask mask-squircle w-12 h-12" src={t.imageurl} alt="Avatar" /></td>
        <td>{t.lat}</td>
        <td>{t.lng}</td>

      </tr>))}
    </tbody>
  </table>
</div>
        </div>
      </body>
    </div>
  );
}

export default App;
