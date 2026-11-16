import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ClientsService } from '../services/ClientsService';

export default function NewClientPage() {
  const navigate = useNavigate();
  const [client, setClient] = useState({
    name: '',
    email: '',
    phone: ''
  });
  const [saving, setSaving] = useState(false);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const save = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!client.name.trim() || !client.email.trim()) {
      alert('Por favor completa al menos el nombre y el correo.');
      return;
    }
    try {
      setSaving(true);
      setErrorMsg(null);
      await ClientsService.addClient(client);
      navigate('/clients');
    } catch (err: any) {
      console.error('Error al guardar cliente:', err);
      setErrorMsg(err.message || 'Error al guardar el cliente en Supabase.');
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="container mt-4 mb-5">
      <div className="row justify-content-center">
        <div className="col-md-7">
          <div className="card shadow-sm border-0">
            <div className="card-header bg-primary text-white py-3">
              <h4 className="mb-0">Añadir Nuevo Cliente</h4>
            </div>
            <div className="card-body p-4">
              {errorMsg && (
                <div className="alert alert-danger" role="alert">
                  {errorMsg}
                </div>
              )}
              <form onSubmit={save}>
                <div className="mb-3">
                  <label className="form-label fw-semibold">Nombre completo</label>
                  <input
                    type="text"
                    className="form-control"
                    placeholder="Ej. Juan Pérez"
                    required
                    value={client.name}
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
                    placeholder="Ej. juan@test.com"
                    required
                    value={client.email}
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
                    placeholder="Ej. 600111111"
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
                    Cancelar
                  </Link>
                  <button
                    type="submit"
                    className="btn btn-success px-4"
                    disabled={saving}
                  >
                    {saving ? 'Guardando...' : 'Guardar Cliente'}
                  </button>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
