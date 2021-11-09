import { BrowserRouter, Route, Routes } from 'react-router-dom';
import IndexPage from './pages/index_page.js';
import RegisterPage from './pages/register_page.js';
// para funcionar no Router que que import com a mesmo o nome
function Router() {
  return (
    <BrowserRouter>
      <Routes>
      
        <Route path="/" exact element={<IndexPage />} /> 
        <Route path="/register" element={<RegisterPage />} />

      </Routes>
     
    </BrowserRouter>
  )
}


export default Router;
