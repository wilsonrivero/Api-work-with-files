import React, {useState} from 'react';
import axios from 'axios';
import {Form} from '@unform/web';



function RegisterPage() {
  const [inputs, setInputs] = useState({});
  const [file, setFile] = useState()

  const handleChange = (e) => {
      const name = e.target.name;
      const value = e.target.value;
      setInputs(values => ({...values, [name]: value}))
  }
  const handleChangeFile = (event) => {
		const file = event.target.files[0]
      setFile(file)
  }
  const handleSubmit = (event) => {
    event.preventDefault();
  
    const form_data = new FormData()
    form_data.append('name', inputs.name)
    form_data.append('cpf', inputs.cpf)
    form_data.append('age', inputs.age)
    form_data.append('file', file)

    console.log(form_data)
    axios.post('http://127.0.0.1:8000/register', form_data).then(req => {
      console.log(req.data)
    })
  }
    
  return (
    <form onSubmit={handleSubmit} encType='multipart/form-data'>
      <label>Enter your name:
        <input 
          type="text" 
          name="name" 
          value={inputs.name || ""}
          onChange={handleChange}
        />
      </label>
      <label>Enter your cpf:
        <input 
          type="text" 
          name="cpf"
          value={inputs.cpf || ""} 
          onChange={handleChange}
        />
      </label>

      <label>Enter your age:
            <input 
              type="number" 
              name="age" 
              value={inputs.age || ""}
              onChange={handleChange}
          />
      </label>

		 <label>Enter your Image:
            <input 
              type="file" 
            name="file" 
            value={inputs.file || ""} 
            onChange={handleChangeFile}
          />
      </label>



      <input type="submit" />
    </form>
  )
}

export default RegisterPage;
