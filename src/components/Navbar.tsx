import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary shadow-sm mb-4">
      <div className="container">
        <NavLink className="navbar-brand fw-bold" to="/clients">
          AppClients
        </NavLink>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav ms-auto">
            <li className="nav-item">
              <NavLink
                to="/clients"
                className={({ isActive }) =>
                  `nav-link ${isActive ? 'active fw-semibold' : ''}`
                }
              >
                Ver clientes
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/new-client"
                className={({ isActive }) =>
                  `nav-link ${isActive ? 'active fw-semibold' : ''}`
                }
              >
                Añadir clientes
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink
                to="/about"
                className={({ isActive }) =>
                  `nav-link ${isActive ? 'active fw-semibold' : ''}`
                }
              >
                About
              </NavLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
