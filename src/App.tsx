import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from 'react-router-dom';
import ClientsPage from './pages/ClientsPage';
import NewClientPage from './pages/NewClientPage';
import EditClientPage from './pages/EditClientPage';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/clients" />} />
        <Route path="/clients" element={<ClientsPage />} />
        <Route path="/new-client" element={<NewClientPage />} />
        <Route path="/edit-client/:id" element={<EditClientPage />} />
      </Routes>
    </BrowserRouter>
  );
}
