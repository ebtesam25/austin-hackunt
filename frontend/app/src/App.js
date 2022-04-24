import logo from './logo.svg';
import './App.css';
import Navbar from './components/navbar';
import Options from './components/options';

function App() {
  return (
    <div className="App">
      <header>
      <Navbar/>
      </header>
      <body className="bg-blue-900">
        <div className="grid place-items-center h-screen">
        <Options/>
        </div>
      </body>
    </div>
  );
}

export default App;
