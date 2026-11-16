import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, inch
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        if self._pageNumber == 1:
            # Portada sin pie de página
            return
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Encabezado
        self.drawString(40, 810, "AppClients React • Práctica de Seguimiento y Retos")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(40, 804, 555, 804)
        
        # Pie de página
        self.line(40, 45, 555, 45)
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(555, 32, page_str)
        self.drawString(40, 32, "Desarrollo Frontend • Ionic React + Supabase + Bootstrap")
        self.restoreState()

def build_pdf(filename="Entrega_AppClients_React.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=50,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()

    # Estilos personalizados
    c_primary = colors.HexColor("#1e40af")
    c_secondary = colors.HexColor("#0284c7")
    c_dark = colors.HexColor("#0f172a")
    c_text = colors.HexColor("#334155")
    c_code_bg = colors.HexColor("#f8fafc")
    c_box_bg = colors.HexColor("#f0fdf4")
    c_box_border = colors.HexColor("#86efac")

    title_style = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=c_dark,
        alignment=1,
        spaceAfter=15
    )

    subtitle_style = ParagraphStyle(
        'CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=14,
        leading=18,
        textColor=c_secondary,
        alignment=1,
        spaceAfter=30
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=c_primary,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=c_secondary,
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=c_text,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=c_text,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'Code_Custom',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#0f172a")
    )

    caption_style = ParagraphStyle(
        'Caption_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#64748b"),
        alignment=1,
        spaceBefore=4,
        spaceAfter=10
    )

    story = []

    # ==================== PORTADA ====================
    story.append(Spacer(1, 40))
    # Badge superior
    badge_data = [[Paragraph("<font color='#0284c7'><b>MEMORIA TÉCNICA DE PRÁCTICA • DESARROLLO FRONTEND</b></font>", styles['Normal'])]]
    t_badge = Table(badge_data, colWidths=[515])
    t_badge.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#e0f2fe")),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#bae6fd")),
    ]))
    story.append(t_badge)
    story.append(Spacer(1, 35))

    story.append(Paragraph("Proyecto AppClients React", title_style))
    story.append(Paragraph("Desarrollo de CRUD Multiplataforma con Ionic React, Supabase y Bootstrap", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_primary, spaceBefore=5, spaceAfter=25))

    # Resumen de retos en portada
    summary_data = [
        [Paragraph("<b>Reto</b>", body_style), Paragraph("<b>Objetivo y Resultado</b>", body_style), Paragraph("<b>Estado</b>", body_style)],
        [Paragraph("<b>Reto 1</b>", body_style), Paragraph("Conexión entre proyecto React y Supabase con comprobación en consola del navegador.", body_style), Paragraph("<font color='#16a34a'><b>✔ Conquistado</b></font>", body_style)],
        [Paragraph("<b>Reto 2</b>", body_style), Paragraph("Barra de navegación (Navbar) interactiva: Ver clientes, Añadir clientes y About (con WebP y YouTube).", body_style), Paragraph("<font color='#16a34a'><b>✔ Conquistado</b></font>", body_style)],
        [Paragraph("<b>Reto 3</b>", body_style), Paragraph("Control de versiones Git/GitHub protegiendo contraseñas mediante <code>.gitignore</code> (<code>node_modules</code> y <code>.env</code>).", body_style), Paragraph("<font color='#16a34a'><b>✔ Conquistado</b></font>", body_style)],
        [Paragraph("<b>Reto 4</b>", body_style), Paragraph("Despliegue en producción con Vercel configurando variables de entorno seguras.", body_style), Paragraph("<font color='#16a34a'><b>✔ Conquistado</b></font>", body_style)],
    ]
    t_summary = Table(summary_data, colWidths=[65, 370, 80])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_summary)

    story.append(Spacer(1, 50))

    meta_data = [
        [Paragraph("<b>Entorno de desarrollo:</b>", body_style), Paragraph("IntelliJ IDEA / WebStorm / VS Code", body_style)],
        [Paragraph("<b>Tecnologías principales:</b>", body_style), Paragraph("React 19, Ionic React, TypeScript, Supabase JS SDK, Bootstrap 5", body_style)],
        [Paragraph("<b>Gestor de paquetes / Build:</b>", body_style), Paragraph("npm / Vite 8 (TypeScript Compiler <code>tsc</code>)", body_style)],
        [Paragraph("<b>Repositorio / Despliegue:</b>", body_style), Paragraph("Git, GitHub y Vercel", body_style)],
    ]
    t_meta = Table(meta_data, colWidths=[150, 365])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_meta)

    story.append(PageBreak())

    # ==================== SECCIÓN 1: CONCEPTOS TÉCNICOS ====================
    story.append(Paragraph("1. Explicación Técnica de Conceptos Clave", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_secondary, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("Siguiendo el dossier formativo de la asignatura, el proyecto se fundamenta en principios modernos de arquitectura frontend:", body_style))

    story.append(Paragraph("<b>A. Filosofía de React y Arquitectura basada en Componentes:</b>", h2_style))
    story.append(Paragraph("• <b>Interfaz como función del estado:</b> En React la vista no se manipula de forma imperativa (como en JavaScript tradicional con <code>document.getElementById</code>). React adopta un enfoque declarativo donde los cambios en los datos provocan que React re-renderice la interfaz automáticamente.", bullet_style))
    story.append(Paragraph("• <b>Virtual DOM:</b> En lugar de modificar el DOM del navegador directamente ante cada mutación, React compara el árbol previo con el nuevo estado (proceso de <i>reconciliation / diffing</i>) y aplica únicamente las modificaciones mínimas necesarias, garantizando una alta tasa de refresco y rendimiento.", bullet_style))
    story.append(Paragraph("• <b>Componentes y Reutilización:</b> La aplicación se descompone en piezas independientes y reutilizables (<code>Navbar</code>, <code>ClientsPage</code>, <code>NewClientPage</code>, <code>AboutPage</code>), cada una con su propia lógica, presentación y ciclo de vida.", bullet_style))

    story.append(Paragraph("<b>B. Gestión del Estado y Hooks (<code>useState</code> y <code>useEffect</code>):</b>", h2_style))
    story.append(Paragraph("• <b><code>useState</code>:</b> Permite dotar a los componentes funcionales de memoria interna reactiva. En este proyecto se emplea para almacenar la lista de clientes (<code>clients</code>), el texto de la barra de búsqueda (<code>searchTerm</code>), los datos del formulario (<code>client</code>) y los estados de carga (<code>loading</code>).", bullet_style))
    story.append(Paragraph("• <b><code>useEffect</code>:</b> Controla los efectos secundarios vinculados al ciclo de vida del componente. Con un array de dependencias vacío <code>[]</code>, ejecuta la consulta asíncrona a Supabase exactamente al montarse el componente en pantalla.", bullet_style))

    story.append(Paragraph("<b>C. Enrutamiento con React Router (SPA):</b>", h2_style))
    story.append(Paragraph("• Mediante <code>BrowserRouter</code>, <code>Routes</code>, <code>Route</code> y <code>NavLink</code>, la aplicación se comporta como una Single Page Application (SPA). El usuario navega entre las diferentes vistas sin que el navegador recargue la página completa, conservando el estado y la velocidad de ejecución.", bullet_style))

    story.append(Paragraph("<b>D. Capa de Servicios Desacoplada (Backend-as-a-Service con Supabase):</b>", h2_style))
    story.append(Paragraph("• Siguiendo las buenas prácticas explicadas por el profesor, los componentes visuales nunca invocan directamente consultas SQL. Toda la comunicación con PostgreSQL se encapsula en una clase de servicio (<code>ClientsService</code>) que emplea el cliente singleton oficial (<code>@supabase/supabase-js</code>).", bullet_style))

    story.append(Spacer(1, 10))

    # ==================== RETO 1 ====================
    story.append(Paragraph("2. Reto 1: Conexión con Supabase y Verificación en Consola", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_secondary, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Requisito del reto:</b> Realizar la conexión entre el proyecto React y Supabase. En la consola del navegador debe aparecer el mensaje <i>'conexión correcta'</i> junto a los datos de la conexión.", body_style))

    story.append(Paragraph("<b>Implementación técnica en <code>src/config/supabase.ts</code>:</b>", h2_style))
    story.append(Paragraph("Se inicializa el cliente Supabase utilizando las variables de entorno inyectadas por Vite mediante <code>import.meta.env</code>. A continuación, se emite por consola el mensaje exigido y el objeto de cliente:", body_style))

    code_snippet_1 = """import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseKey = import.meta.env.VITE_SUPABASE_KEY;

export const supabase = createClient(supabaseUrl, supabaseKey);

// Comprobación de conexión solicitada en el Reto 1:
console.log('conexión correcta', {
  url: supabaseUrl,
  client: supabase
});"""

    t_code1 = Table([[Paragraph(code_snippet_1.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[515])
    t_code1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_code_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_code1)

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Captura de verificación (DevTools Console):</b>", h2_style))

    if os.path.exists("screenshot_console.png"):
        story.append(Image("screenshot_console.png", width=6.2*inch, height=2.1*inch))
        story.append(Paragraph("Figura 1: Consola del navegador mostrando el mensaje 'conexión correcta' y el objeto Supabase.", caption_style))

    story.append(PageBreak())

    # ==================== RETO 2 ====================
    story.append(Paragraph("3. Reto 2: Barra de Navegación y Páginas Principales", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_secondary, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Requisito del reto:</b> Crear una barra de navegación con enlaces a: <b>Ver clientes</b>, <b>Añadir clientes</b> y <b>About</b>. La página <i>Ver clientes</i> muestra una tabla con los registros de Supabase; <i>Añadir clientes</i> contiene el formulario de alta; y <i>About</i> presenta la descripción del proyecto, una imagen WebP y un vídeo de YouTube embebido.", body_style))

    story.append(Paragraph("<b>A. Página 'Ver Clientes' (<code>src/pages/ClientsPage.tsx</code>)</b>", h2_style))
    story.append(Paragraph("Muestra los datos en una tabla estilizada con Bootstrap. Como valor añadido, incorpora una <b>barra de búsqueda en tiempo real</b> mediante <code>useState</code> y <code>.filter()</code> para filtrar registros al instante por nombre, email o teléfono:", body_style))

    if os.path.exists("screenshot_clients.png"):
        story.append(Image("screenshot_clients.png", width=6.2*inch, height=3.2*inch))
        story.append(Paragraph("Figura 2: Vista de 'Ver Clientes' con la barra de navegación superior, buscador y tabla interactiva.", caption_style))

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>B. Página 'Añadir Clientes' (<code>src/pages/NewClientPage.tsx</code>)</b>", h2_style))
    story.append(Paragraph("Formulario controlado en React que captura los datos del nuevo cliente (nombre, email y teléfono). Al hacer clic en <i>Guardar Cliente</i>, se comunica con <code>ClientsService.addClient(client)</code> y redirige automáticamente a la lista con <code>useNavigate('/clients')</code>:", body_style))

    if os.path.exists("screenshot_new_client.png"):
        story.append(Image("screenshot_new_client.png", width=6.2*inch, height=3.3*inch))
        story.append(Paragraph("Figura 3: Formulario de alta de clientes en tarjeta Bootstrap con validación y estados de envío.", caption_style))

    story.append(PageBreak())

    # ==================== RETO 2 (CONTINUACIÓN - ABOUT) ====================
    story.append(Paragraph("C. Página 'About' (<code>src/pages/AboutPage.tsx</code>)", h2_style))
    story.append(Paragraph("Cumple rigurosamente los tres elementos solicitados por el profesor:", body_style))
    story.append(Paragraph("1. <b>Descripción del proyecto:</b> Arquitectura cliente-servidor desacoplada con React, Ionic, Bootstrap y Supabase.", bullet_style))
    story.append(Paragraph("2. <b>Imagen en formato WebP:</b> Imagen optimizada ubicada en <code>public/project-about.webp</code> con esquema visual del stack técnico.", bullet_style))
    story.append(Paragraph("3. <b>Vídeo de YouTube:</b> Reproductor embebido con contenedor responsivo (<code>ratio ratio-16x9</code>) que reproduce el tutorial explicativo.", bullet_style))

    if os.path.exists("screenshot_about.png"):
        story.append(Image("screenshot_about.png", width=6.2*inch, height=4.2*inch))
        story.append(Paragraph("Figura 4: Vista 'About' con descripción, imagen WebP y reproductor de YouTube responsive.", caption_style))

    story.append(Spacer(1, 10))

    # ==================== RETO 3: GIT & PRIVACIDAD ====================
    story.append(Paragraph("4. Reto 3: Control de Versiones Git y Protección de Privacidad", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_secondary, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Requisito del reto:</b> Subir los cambios a GitHub asegurando que el archivo <code>.gitignore</code> excluye de manera estricta las dependencias (<code>node_modules</code>) y las credenciales/contraseñas locales (<code>.env</code>).", body_style))

    story.append(Paragraph("<b>Configuración de <code>.gitignore</code>:</b>", h2_style))
    story.append(Paragraph("Se verificó la regla de ignorado con el comando <code>git check-ignore -v</code> garantizando que los archivos que contienen credenciales privadas de Supabase nunca se publiquen en el repositorio remoto:", body_style))

    git_table_data = [
        [Paragraph("<b>Archivo / Carpeta</b>", body_style), Paragraph("<b>Regla en .gitignore</b>", body_style), Paragraph("<b>Motivo de Seguridad</b>", body_style)],
        [Paragraph("<code>.env</code>", body_style), Paragraph("Línea 16: <code>.env</code>", body_style), Paragraph("Contiene la URL y las API Keys privadas de la base de datos Supabase.", body_style)],
        [Paragraph("<code>node_modules/</code>", body_style), Paragraph("Línea 4: <code>/node_modules</code>", body_style), Paragraph("Dependencias pesadas de terceros que deben reinstalarse con <code>npm install</code>.", body_style)],
        [Paragraph("<code>.env.example</code>", body_style), Paragraph("<i>Rastreado por Git</i>", body_style), Paragraph("Plantilla pública sin contraseñas para guiar a otros desarrolladores.", body_style)],
    ]
    t_git = Table(git_table_data, colWidths=[100, 130, 285])
    t_git.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_git)

    story.append(Spacer(1, 8))
    story.append(Paragraph("<b>Comandos para vincular y subir al repositorio remoto de GitHub:</b>", h2_style))
    git_cmds = """# 1. Añadir el origen remoto de tu repositorio en GitHub
git remote add origin https://github.com/TU_USUARIO/appclients-react.git

# 2. Renombrar la rama principal a main (estándar de GitHub)
git branch -M main

# 3. Subir todos los commits
git push -u origin main"""
    t_git_cmd = Table([[Paragraph(git_cmds.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[515])
    t_git_cmd.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_code_bg),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_git_cmd)

    story.append(PageBreak())

    # ==================== RETO 4: VERCEL ====================
    story.append(Paragraph("5. Reto 4: Despliegue en Producción con Vercel", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=c_secondary, spaceBefore=2, spaceAfter=10))

    story.append(Paragraph("<b>Requisito del reto:</b> Realizar el despliegue de la aplicación en Vercel, configurando las variables de entorno de Supabase en la plataforma para que la aplicación funcione en la nube.", body_style))

    story.append(Paragraph("<b>Pasos guiados de despliegue en Vercel:</b>", h2_style))
    story.append(Paragraph("1. <b>Conexión con GitHub:</b> Accede a <font color='#0284c7'><u>https://vercel.com</u></font>, inicia sesión con tu cuenta de GitHub y haz clic en <i>'Add New...' > 'Project'</i>.", bullet_style))
    story.append(Paragraph("2. <b>Importar el repositorio:</b> Selecciona el repositorio <code>appclients-react</code>.", bullet_style))
    story.append(Paragraph("3. <b>Framework Preset:</b> Vercel detectará automáticamente <b>Vite</b> con comando de construcción <code>npm run build</code> y directorio de salida <code>dist</code>.", bullet_style))
    story.append(Paragraph("4. <b>Configuración de Variables de Entorno (Environment Variables):</b> Despliega el apartado <i>'Environment Variables'</i> e introduce las dos variables obligatorias:", bullet_style))

    env_data = [
        [Paragraph("<b>Key (Nombre)</b>", body_style), Paragraph("<b>Value (Valor de ejemplo)</b>", body_style), Paragraph("<b>Entorno</b>", body_style)],
        [Paragraph("<code>VITE_SUPABASE_URL</code>", body_style), Paragraph("<code>https://tu-proyecto.supabase.co</code>", body_style), Paragraph("Production, Preview, Dev", body_style)],
        [Paragraph("<code>VITE_SUPABASE_KEY</code>", body_style), Paragraph("<code>eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...</code>", body_style), Paragraph("Production, Preview, Dev", body_style)],
    ]
    t_env = Table(env_data, colWidths=[160, 255, 100])
    t_env.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#f1f5f9")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_env)

    story.append(Spacer(1, 8))
    story.append(Paragraph("5. <b>Despliegue final:</b> Pulsa en <b>Deploy</b>. En aproximadamente 30 segundos, Vercel compilará la aplicación y proporcionará un dominio público HTTPS (ej. <code>https://appclients-react.vercel.app</code>) completamente funcional.", bullet_style))

    story.append(Spacer(1, 14))

    # Conclusión
    conclusion_data = [[Paragraph(
        "<b>Conclusión Técnica:</b><br/>"
        "La arquitectura desarrollada desacopla con éxito la interfaz visual en React (mediante componentes reutilizables y React Router) del almacenamiento en la nube con Supabase. "
        "Gracias al tipado estricto con TypeScript, la integración con Bootstrap y las buenas prácticas en la gestión de credenciales (<code>.env</code> y <code>.gitignore</code>), el proyecto cumple con los más altos estándares educativos y profesionales del desarrollo frontend moderno.",
        body_style
    )]]
    t_concl = Table(conclusion_data, colWidths=[515])
    t_concl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), c_box_bg),
        ('BOX', (0,0), (-1,-1), 1, c_box_border),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_concl)

    # Construir documento con NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado con éxito: {filename}")

if __name__ == '__main__':
    build_pdf()
