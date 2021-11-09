import React, {useRef} from 'react';
import axios from 'axios';
import {Form} from '@unform/web';
import Input from '../components/input.js';




function RegisterPage () {
  const formRef = useRef(null)
  function handleSubmit(data) {
    //console.log(data)

    const formData = new FormData()
       formData.append('file', data.file)

    //console.log(formData)
    axios.post('http://127.0.0.1:8000/register', formData ).then(req => {
      console.log(req.data)
    }).catch(req => {
      console.log(req)
    })

  }


  return (
    <div className="App">
      <h1>Register Page</h1>

      <Form method="POST" ref={formRef} onSubmit={handleSubmit}  encType='multipart/form-data'>
        <div>
          <label htmlFor="name">Nome:</label>
          <Input type="text" name="name"/>
        </div> 

        <div>
          <label htmlFor="age">Cpf:</label>
          <Input type="text" name="cpf"/>
        </div> 

        <div>
          <label htmlFor="age">Age:</label>
          <Input type="number" name="age"/>
        </div> 
        <div>
          <label htmlFor="file">File:</label>
          <Input type="file" name="file"/>
        </div> 
        <button type="submit">Enviar</button>
      </Form>
    </div>

  )
}
export default RegisterPage;
