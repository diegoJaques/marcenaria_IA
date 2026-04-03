import { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { listProjects } from '../services/api'

export default function ProjectListPage() {
  const [projects, setProjects] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    loadProjects()
  }, [])

  const loadProjects = async () => {
    try {
      setLoading(true)
      const data = await listProjects()
      setProjects(data)
    } catch (err) {
      setError('Erro ao carregar projetos')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return (
      <div className="text-center py-20">
        <div className="spinner w-16 h-16 mx-auto mb-4"></div>
        <p className="text-xl text-gray-600">Carregando seus projetos...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-red-50 border-2 border-red-300 rounded-2xl p-8 text-center">
        <div className="text-6xl mb-4">❌</div>
        <h2 className="text-2xl font-bold text-red-900 mb-2">Ops!</h2>
        <p className="text-red-800">{error}</p>
        <button
          onClick={loadProjects}
          className="mt-4 btn-primary"
        >
          Tentar Novamente
        </button>
      </div>
    )
  }

  if (projects.length === 0) {
    return (
      <div className="text-center py-20">
        <div className="text-8xl mb-6">📭</div>
        <h2 className="text-3xl font-bold text-gray-900 mb-4">
          Nenhum projeto ainda
        </h2>
        <p className="text-xl text-gray-600 mb-8">
          Que tal criar seu primeiro projeto?
        </p>
        <Link to="/new" className="btn-primary inline-block">
          <span className="text-2xl mr-2">✨</span>
          Criar Primeiro Projeto
        </Link>
      </div>
    )
  }

  return (
    <div>
      {/* Header */}
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-4xl font-bold text-gray-900 mb-2">
            📚 Meus Projetos
          </h1>
          <p className="text-gray-600">
            Você tem {projects.length} projeto{projects.length !== 1 ? 's' : ''}
          </p>
        </div>
        <Link to="/new" className="btn-primary">
          <span className="text-xl mr-2">➕</span>
          Novo Projeto
        </Link>
      </div>

      {/* Grade de Projetos */}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
        {projects.map(project => (
          <Link
            key={project.id}
            to={`/projects/${project.id}`}
            className="bg-white rounded-2xl shadow-lg hover:shadow-2xl transition-all duration-200 overflow-hidden group"
          >
            {/* Imagem */}
            <div className="aspect-square bg-gray-100 relative overflow-hidden">
              {project.thumbnail_url ? (
                <img
                  src={project.thumbnail_url}
                  alt={`Projeto ${project.furniture_type}`}
                  className="w-full h-full object-cover group-hover:scale-110 transition-transform duration-300"
                />
              ) : (
                <div className="w-full h-full flex items-center justify-center text-gray-400">
                  <span className="text-6xl">🖼️</span>
                </div>
              )}

              {/* Badge de número de imagens */}
              {project.images_count > 0 && (
                <div className="absolute top-3 right-3 bg-black bg-opacity-70 text-white px-3 py-1 rounded-full text-sm font-semibold">
                  📸 {project.images_count}
                </div>
              )}
            </div>

            {/* Detalhes */}
            <div className="p-5">
              <div className="flex items-start justify-between mb-3">
                <div>
                  <h3 className="font-bold text-lg capitalize">
                    {project.furniture_type}
                  </h3>
                  <p className="text-sm text-gray-600 capitalize">
                    {project.room} • {project.style}
                  </p>
                </div>
              </div>

              {project.client_name && (
                <div className="text-sm text-gray-600 mb-2">
                  <span className="font-semibold">Cliente:</span> {project.client_name}
                </div>
              )}

              <div className="text-xs text-gray-500">
                {new Date(project.created_at).toLocaleDateString('pt-BR', {
                  day: '2-digit',
                  month: 'short',
                  year: 'numeric'
                })}
              </div>

              <div className="mt-4 text-wood-600 font-semibold group-hover:text-wood-700">
                Ver Detalhes →
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
