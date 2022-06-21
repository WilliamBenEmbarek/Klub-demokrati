import './App.css';
import ClubDemokrati from './Components/ClubDemokrati.js';
import AdminPanel from './Components/AdminPanel';
function App() {

  if (window.location.pathname === "/admin") {
    return(
      <AdminPanel/>
    )
  }

  return (
    <div className="App">
      <header className="App-header">
      <meta name="viewport" content="width=device-width, initial-scale=1"/> 
      <ClubDemokrati/>
      </header>
    </div>
  );
}

export default App;
