import React, {useState,useEffect} from 'react';
import axios from 'axios';



// Para funcionar tem que oclocara exatamente o mesmo nome
function IndexPage() {
  const [clients, setClients] = useState([])

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/').then(req => {
      console.log(req.data.Clients)
      setClients(req.data.Clients)
    })    

  }, [])
  
  return (
    <div className="App">
      <h1>Index Page</h1>
      <div>
      {clients.map(data => {
          return (
            <div>
            <h2>{data.Client.name}</h2>
            <span>{data.Client.cpf}</span>
              <button  onClick={() => {
                axios.delete(`http://127.0.0.1:8000/delete/${data.Client._id}`).then(req => {
                  window.location.reload(true)
                }).catch(e => {
                  console.log(e)
                }) 
              }} >Delete</button>


            {data.Images.map(image => {
                return (
                  <div>
                    <h3>{image.name}</h3>
                    <img  src={`data:image/jpg;base64,${image.rendered_data}`} alt="img" />
                  </div>
                )
            })}
            </div>
          )

        })}
      </div>
    </div>  
  )
}

export default IndexPage;
