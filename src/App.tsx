import {
  BrowserRouter,
  Routes,
  Route,
  Navigate
} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Navbar from './components/Navbar';
import ClientsPage from './pages/ClientsPage';
import NewClientPage from './pages/NewClientPage';
import EditClientPage from './pages/EditClientPage';
import AboutPage from './pages/AboutPage';

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Navigate to="/clients" replace />} />
        <Route path="/clients" element={<ClientsPage />} />
        <Route path="/new-client" element={<NewClientPage />} />
        <Route path="/edit-client/:id" element={<EditClientPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="*" element={<Navigate to="/clients" replace />} />
      </Routes>
    </BrowserRouter>
  );
}
