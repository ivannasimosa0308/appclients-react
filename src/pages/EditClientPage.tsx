import { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ClientsService } from '../services/ClientsService';

export default function EditClientPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [client, setClient] = useState({
    name: '',
    email: '',
    phone: ''
  });

  const loadClient = async () => {
    if (id) {
      const data = await ClientsService.getClient(Number(id));
      if (data) {
        setClient({
          name: data.name || '',
          email: data.email || '',
          phone: data.phone || ''
        });
      }
    }
  };

  useEffect(() => {
    loadClient();
  }, [id]);

  const update = async () => {
    if (id) {
      await ClientsService.updateClient(Number(id), client);
      navigate('/clients');
    }
  };

  return (
    <div className="container mt-4">
      <h2>Modificar Cliente</h2>
      <input
        className="form-control mb-2"
        placeholder="Nombre"
        value={client.name}
        onChange={(e) =>
          setClient({
            ...client,
            name: e.target.value
          })
        }
      />
      <input
        className="form-control mb-2"
        placeholder="Email"
        value={client.email}
        onChange={(e) =>
          setClient({
            ...client,
            email: e.target.value
          })
        }
      />
      <input
        className="form-control mb-2"
        placeholder="Teléfono"
        value={client.phone}
        onChange={(e) =>
          setClient({
            ...client,
            phone: e.target.value
          })
        }
      />
      <button className="btn btn-success" onClick={update}>
        Actualizar
      </button>
    </div>
  );
}
