import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import HomePage from './pages/HomePage'
import NewProjectPage from './pages/NewProjectPage'
import ProjectListPage from './pages/ProjectListPage'
import ProjectDetailPage from './pages/ProjectDetailPage'

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gradient-to-b from-wood-50 to-gray-100">
        {/* Header Simples */}
        <header className="bg-wood-700 text-white shadow-lg">
          <div className="container-main">
            <div className="flex items-center justify-between py-6">
              <Link to="/" className="flex items-center space-x-3">
                <span className="text-4xl">🪵</span>
                <div>
                  <h1 className="text-2xl md:text-3xl font-bold">MarcenAI</h1>
                  <p className="text-sm text-wood-200">Seus projetos com inteligência</p>
                </div>
              </Link>

              <Link
                to="/projects"
                className="flex items-center space-x-2 bg-wood-600 hover:bg-wood-500 px-4 py-2 rounded-lg transition"
              >
                <span className="text-2xl">📚</span>
                <span className="hidden md:inline">Meus Projetos</span>
              </Link>
            </div>
          </div>
        </header>

        {/* Conteúdo Principal */}
        <main className="container-main py-8">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/new" element={<NewProjectPage />} />
            <Route path="/projects" element={<ProjectListPage />} />
            <Route path="/projects/:id" element={<ProjectDetailPage />} />
          </Routes>
        </main>

        {/* Footer Simples */}
        <footer className="bg-white border-t mt-16 py-6">
          <div className="container-main text-center text-gray-600 text-sm">
            <p>🪵 Desenvolvido para facilitar o trabalho de marceneiros</p>
            <p className="mt-2 text-xs">Projeto de Extensão II - Diego Jaques Tinoco</p>
          </div>
        </footer>
      </div>
    </Router>
  )
}

export default App
