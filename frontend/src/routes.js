import { BrowserRouter, Route, Routes } from 'react-router-dom';
import IndexPage from './pages/index_page.js';


function Router() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" exact element={<IndexPage />} /> 

      </Routes>
     
    </BrowserRouter>
  )
}


export default Router;
