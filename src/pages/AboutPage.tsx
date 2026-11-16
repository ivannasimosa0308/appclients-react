export default function AboutPage() {
  return (
    <div className="container mt-4 mb-5">
      <div className="row justify-content-center">
        <div className="col-lg-10">
          <div className="card shadow-sm border-0 mb-4">
            <div className="card-body p-4">
              <h2 className="card-title text-primary fw-bold mb-3">
                Acerca de AppClients React
              </h2>
              <p className="lead text-secondary">
                Aplicación web y móvil desarrollada con <strong>React</strong>,{' '}
                <strong>Ionic</strong>, <strong>TypeScript</strong> y{' '}
                <strong>Supabase</strong> como Backend-as-a-Service (BaaS).
              </p>
              <hr />
              <h5>Descripción del Proyecto</h5>
              <p>
                Este proyecto implementa una arquitectura moderna orientada a la
                gestión completa de clientes (CRUD: Crear, Leer, Actualizar y
                Eliminar). La capa visual utiliza <strong>Bootstrap</strong>{' '}
                junto con los componentes de Ionic, comunicándose a través de
                un servicio desacoplado (<code>ClientsService</code>) que
                interactúa con la base de datos PostgreSQL alojada en Supabase mediante su SDK oficial.
              </p>
              <p>
                La navegación está gestionada mediante{' '}
                <strong>React Router</strong> con una barra de navegación común,
                rutas declarativas y protección de variables de entorno mediante
                Vite.
              </p>
            </div>
          </div>

          {/* Imagen en formato WebP requerida */}
          <div className="card shadow-sm border-0 mb-4">
            <div className="card-header bg-white fw-bold py-3">
              Arquitectura y Stack Tecnológico (.webp)
            </div>
            <div className="card-body text-center p-3">
              <img
                src="/project-about.webp"
                alt="Diagrama de Arquitectura del Proyecto"
                className="img-fluid rounded border shadow-sm"
                style={{ maxHeight: '420px', width: '100%', objectFit: 'contain' }}
              />
              <p className="text-muted small mt-2">
                Imagen optimizada en formato WebP alojada en <code>public/project-about.webp</code>
              </p>
            </div>
          </div>

          {/* Vídeo de YouTube requerido */}
          <div className="card shadow-sm border-0">
            <div className="card-header bg-white fw-bold py-3">
              Vídeo Explicativo: Introducción a Supabase y React
            </div>
            <div className="card-body p-3">
              <div className="ratio ratio-16x9 rounded overflow-hidden shadow-sm">
                <iframe
                  src="https://www.youtube.com/embed/b-h_v3SZ8w8"
                  title="Tutorial React y Supabase"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowFullScreen
                ></iframe>
              </div>
              <p className="text-muted small mt-2">
                Vídeo explicativo integrado mediante iframe responsivo de Bootstrap.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
