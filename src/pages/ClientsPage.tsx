import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ClientsService } from '../services/ClientsService';
import { Client } from '../interfaces/Client';

export default function ClientsPage() {
  const [clients, setClients] = useState<Client[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const loadClients = async () => {
    try {
      setLoading(true);
      setErrorMessage(null);
      const data = await ClientsService.getClients();
      setClients(data || []);
    } catch (error: any) {
      console.error('Error al cargar clientes:', error);
      setErrorMessage(
        error.message || 'No se pudieron cargar los clientes de Supabase.'
      );
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadClients();
  }, []);

  const remove = async (id: number) => {
    const ok = confirm('¿Eliminar cliente?');
    if (!ok) return;
    try {
      await ClientsService.deleteClient(id);
      await loadClients();
    } catch (error: any) {
      alert('Error al eliminar cliente: ' + (error.message || error));
    }
  };

  // Filtrado reactivo en tiempo real
  const filteredClients = clients.filter((client) => {
    const term = searchTerm.toLowerCase();
    return (
      (client.name && client.name.toLowerCase().includes(term)) ||
      (client.email && client.email.toLowerCase().includes(term)) ||
      (client.phone && client.phone.toLowerCase().includes(term))
    );
  });

  return (
    <div className="container mt-4 mb-5">
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h2>Ver Clientes</h2>
        <Link to="/new-client" className="btn btn-primary">
          + Añadir Cliente
        </Link>
      </div>

      {/* Barra de búsqueda integrada */}
      <div className="row mb-3">
        <div className="col-md-6">
          <input
            type="text"
            className="form-control"
            placeholder="Buscar por nombre, email o teléfono..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
      </div>

      {errorMessage && (
        <div className="alert alert-warning" role="alert">
          {errorMessage}
        </div>
      )}

      {loading ? (
        <div className="text-center py-5">
          <div className="spinner-border text-primary" role="status">
            <span className="visually-hidden">Cargando...</span>
          </div>
          <p className="mt-2 text-muted">Cargando clientes de Supabase...</p>
        </div>
      ) : (
        <div className="table-responsive bg-white rounded shadow-sm">
          <table className="table table-bordered table-hover align-middle mb-0">
            <thead className="table-light">
              <tr>
                <th style={{ width: '80px' }}>ID</th>
                <th>Nombre</th>
                <th>Email</th>
                <th>Teléfono</th>
                <th style={{ width: '180px' }}>Acciones</th>
              </tr>
            </thead>
            <tbody>
              {filteredClients.length > 0 ? (
                filteredClients.map((client) => (
                  <tr key={client.id}>
                    <td>{client.id}</td>
                    <td className="fw-semibold">{client.name}</td>
                    <td>{client.email}</td>
                    <td>{client.phone}</td>
                    <td>
                      <Link
                        to={`/edit-client/${client.id}`}
                        className="btn btn-warning btn-sm me-2"
                      >
                        Editar
                      </Link>
                      <button
                        className="btn btn-danger btn-sm"
                        onClick={() => client.id && remove(client.id)}
                      >
                        Eliminar
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan={5} className="text-center py-4 text-muted">
                    {searchTerm
                      ? 'No hay clientes que coincidan con la búsqueda.'
                      : 'No se encontraron clientes registrados en Supabase.'}
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
