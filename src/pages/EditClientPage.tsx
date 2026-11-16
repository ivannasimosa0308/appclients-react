import { useEffect, useState } from 'react';
import { useNavigate, useParams, Link } from 'react-router-dom';
import { ClientsService } from '../services/ClientsService';

export default function EditClientPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [client, setClient] = useState({
    name: '',
    email: '',
    phone: ''
  });
  const [loading, setLoading] = useState(true);
  const [updating, setUpdating] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const loadClient = async () => {
    if (id) {
      try {
        setLoading(true);
        const data = await ClientsService.getClient(Number(id));
        if (data) {
          setClient({
            name: data.name || '',
            email: data.email || '',
            phone: data.phone || ''
          });
        }
      } catch (err: any) {
        console.error('Error al cargar cliente:', err);
        setErrorMsg('No se pudo encontrar el cliente.');
      } finally {
        setLoading(false);
      }
    }
  };

  useEffect(() => {
    loadClient();
  }, [id]);

  const update = async (e: React.FormEvent) => {
    e.preventDefault();
    if (id) {
      try {
        setUpdating(true);
        setErrorMsg(null);
        await ClientsService.updateClient(Number(id), client);
        navigate('/clients');
      } catch (err: any) {
        console.error('Error al actualizar cliente:', err);
        setErrorMsg(err.message || 'Error al actualizar el cliente en Supabase.');
      } finally {
        setUpdating(false);
      }
    }
  };

  return (
    <div className="container mt-4 mb-5">
      <div className="row justify-content-center">
        <div className="col-md-7">
          <div className="card shadow-sm border-0">
            <div className="card-header bg-warning text-dark py-3">
              <h4 className="mb-0">Modificar Cliente #{id}</h4>
            </div>
            <div className="card-body p-4">
              {errorMsg && (
                <div className="alert alert-danger" role="alert">
                  {errorMsg}
                </div>
              )}
              {loading ? (
                <p className="text-center my-4">Cargando datos del cliente...</p>
              ) : (
                <form onSubmit={update}>
                  <div className="mb-3">
                    <label className="form-label fw-semibold">Nombre completo</label>
                    <input
                      type="text"
                      className="form-control"
                      value={client.name}
                      required
                      onChange={(e) =>
                        setClient({
                          ...client,
                          name: e.target.value
                        })
                      }
                    />
                  </div>

                  <div className="mb-3">
                    <label className="form-label fw-semibold">Correo electrónico</label>
                    <input
                      type="email"
                      className="form-control"
                      value={client.email}
                      required
                      onChange={(e) =>
                        setClient({
                          ...client,
                          email: e.target.value
                        })
                      }
                    />
                  </div>

                  <div className="mb-4">
                    <label className="form-label fw-semibold">Teléfono</label>
                    <input
                      type="tel"
                      className="form-control"
                      value={client.phone}
                      onChange={(e) =>
                        setClient({
                          ...client,
                          phone: e.target.value
                        })
                      }
                    />
                  </div>

                  <div className="d-flex justify-content-between">
                    <Link to="/clients" className="btn btn-outline-secondary">
                      Volver
                    </Link>
                    <button
                      type="submit"
                      className="btn btn-warning px-4"
                      disabled={updating}
                    >
                      {updating ? 'Guardando...' : 'Actualizar Cliente'}
                    </button>
                  </div>
                </form>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
