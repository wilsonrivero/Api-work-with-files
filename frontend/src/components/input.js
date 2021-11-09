import { useField } from '@unform/core';
import {useEffect, useRef } from 'react';


function Input({name, ...rest}) {

  const inputRef = useRef(null)

  const {fieldName, registerField, error} = useField(name)

  useEffect(() => {

    registerField({
      name: fieldName,
      ref: inputRef.current,
      path: 'value'
    })
  },  [fieldName, registerField])


  return (
    <div>
      <input ref={inputRef} {...rest}/>
      {error && <span style={{color: '#f00', display: "block"}}>{error}</span>}
    </div>
  )
}


export default Input;
