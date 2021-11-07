import React, {useState,useEffect} from 'react';
import axios from 'axios';


function IndexPage() {
  const [clients, setClients] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/').then(req => {
      console.log(req.data)
    })    

  }, [])


  return (
    <div className="App">
      <h1>Index Page</h1>
    </div>  
  )
}

export default IndexPage;
