import { useState, useEffect } from 'react'
import { useParams, useNavigate, Link } from 'react-router-dom'
import { getProject, refineProject, deleteProject } from '../services/api'

export default function ProjectDetailPage() {
  const { id } = useParams()
  const navigate = useNavigate()

  const [project, setProject] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  const [refining, setRefining] = useState(false)
  const [showRefineForm, setShowRefineForm] = useState(false)
  const [refinementNotes, setRefinementNotes] = useState('')

  useEffect(() => {
    loadProject()
  }, [id])

  const loadProject = async () => {
    try {
      setLoading(true)
      const data = await getProject(id)
      setProject(data)
    } catch (err) {
      setError('Erro ao carregar projeto')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  const handleRefine = async () => {
    if (!refinementNotes.trim()) {
      alert('Por favor, diga o que você quer mudar!')
      return
    }

    try {
      setRefining(true)
      const updatedProject = await refineProject(id, refinementNotes)
      setProject(updatedProject)
      setRefinementNotes('')
      setShowRefineForm(false)
      alert('✨ Nova imagem criada com sucesso!')
    } catch (err) {
      alert('Erro ao refinar projeto. Tente novamente.')
      console.error(err)
    } finally {
      setRefining(false)
    }
  }

  const handleDelete = async () => {
    if (confirm('❗ Tem certeza que quer deletar este projeto? Não poderá desfazer!')) {
      try {
        await deleteProject(id)
        navigate('/projects')
      } catch (err) {
        alert('Erro ao deletar projeto')
        console.error(err)
      }
    }
  }

  if (loading) {
    return (
      <div className="text-center py-20">
        <div className="spinner w-16 h-16 mx-auto mb-4"></div>
        <p className="text-xl text-gray-600">Carregando projeto...</p>
      </div>
    )
  }

  if (error || !project) {
    return (
      <div className="bg-red-50 border-2 border-red-300 rounded-2xl p-8 text-center">
        <div className="text-6xl mb-4">❌</div>
        <h2 className="text-2xl font-bold text-red-900 mb-2">Projeto não encontrado</h2>
        <Link to="/projects" className="btn-primary inline-block mt-4">
          ← Voltar para Projetos
        </Link>
      </div>
    )
  }

  const selectedImage = project.images.find(img => img.is_selected) || project.images[0]

  return (
    <div>
      {/* Header */}
      <div className="flex justify-between items-start mb-8">
        <div>
          <Link to="/projects" className="text-wood-600 hover:text-wood-700 font-semibold mb-2 inline-block">
            ← Voltar para Projetos
          </Link>
          <h1 className="text-4xl font-bold text-gray-900 capitalize mb-2">
            {project.furniture_type}
          </h1>
          <p className="text-xl text-gray-600 capitalize">
            {project.style} para {project.room}
          </p>
        </div>

        <button
          onClick={handleDelete}
          className="bg-red-100 hover:bg-red-200 text-red-700 font-semibold py-3 px-6 rounded-xl transition"
        >
          🗑️ Deletar
        </button>
      </div>

      <div className="grid lg:grid-cols-2 gap-8">
        {/* Imagem Principal */}
        <div>
          <div className="bg-white rounded-2xl shadow-xl overflow-hidden mb-4">
            {selectedImage ? (
              <img
                src={selectedImage.image_url}
                alt="Projeto"
                className="w-full aspect-square object-cover"
              />
            ) : (
              <div className="w-full aspect-square bg-gray-100 flex items-center justify-center">
                <span className="text-8xl text-gray-300">🖼️</span>
              </div>
            )}
          </div>

          {/* Miniaturas (se houver mais de uma imagem) */}
          {project.images.length > 1 && (
            <div className="grid grid-cols-4 gap-3">
              {project.images.map(img => (
                <div
                  key={img.id}
                  className={`aspect-square rounded-lg overflow-hidden cursor-pointer border-3 transition ${
                    img.id === selectedImage?.id
                      ? 'border-wood-600 shadow-lg scale-105'
                      : 'border-transparent hover:border-gray-300'
                  }`}
                >
                  <img
                    src={img.image_url}
                    alt="Variação"
                    className="w-full h-full object-cover"
                  />
                </div>
              ))}
            </div>
          )}

          {/* Botões de Ação */}
          <div className="mt-6 space-y-3">
            {!showRefineForm ? (
              <button
                onClick={() => setShowRefineForm(true)}
                className="w-full btn-primary"
              >
                <span className="text-2xl mr-2">🎨</span>
                Ajustar Imagem
              </button>
            ) : (
              <div className="bg-wood-50 border-2 border-wood-300 rounded-2xl p-6">
                <h3 className="font-bold text-lg mb-3">
                  O que você quer mudar?
                </h3>
                <textarea
                  value={refinementNotes}
                  onChange={(e) => setRefinementNotes(e.target.value)}
                  placeholder="Ex: adicionar mais gavetas, mudar cor para branco, tornar mais rústico..."
                  rows="4"
                  className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none mb-4"
                />

                <div className="flex space-x-3">
                  <button
                    onClick={handleRefine}
                    disabled={refining}
                    className="flex-1 btn-primary"
                  >
                    {refining ? (
                      <>
                        <span className="spinner w-5 h-5 inline-block mr-2"></span>
                        Criando...
                      </>
                    ) : (
                      '✨ Criar Nova Versão'
                    )}
                  </button>
                  <button
                    onClick={() => {
                      setShowRefineForm(false)
                      setRefinementNotes('')
                    }}
                    className="btn-secondary"
                  >
                    Cancelar
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Informações do Projeto */}
        <div>
          <div className="bg-white rounded-2xl shadow-xl p-6 mb-6">
            <h2 className="text-2xl font-bold mb-4">📋 Detalhes do Projeto</h2>

            <div className="space-y-4">
              <div>
                <label className="text-sm font-semibold text-gray-600 uppercase">Móvel</label>
                <p className="text-lg capitalize">{project.furniture_type}</p>
              </div>

              <div>
                <label className="text-sm font-semibold text-gray-600 uppercase">Ambiente</label>
                <p className="text-lg capitalize">{project.room}</p>
              </div>

              <div>
                <label className="text-sm font-semibold text-gray-600 uppercase">Estilo</label>
                <p className="text-lg capitalize">{project.style}</p>
              </div>

              {project.size && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Tamanho</label>
                  <p className="text-lg capitalize">{project.size}</p>
                </div>
              )}

              {project.dimensions && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Dimensões</label>
                  <p className="text-lg">{project.dimensions}</p>
                </div>
              )}

              {project.material && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Material</label>
                  <p className="text-lg">{project.material}</p>
                </div>
              )}

              {project.color && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Cor</label>
                  <p className="text-lg">{project.color}</p>
                </div>
              )}

              {project.special_features && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Características</label>
                  <p className="text-lg">{project.special_features}</p>
                </div>
              )}

              {project.client_name && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Cliente</label>
                  <p className="text-lg">{project.client_name}</p>
                </div>
              )}

              {project.client_notes && (
                <div>
                  <label className="text-sm font-semibold text-gray-600 uppercase">Observações</label>
                  <p className="text-lg">{project.client_notes}</p>
                </div>
              )}

              <div>
                <label className="text-sm font-semibold text-gray-600 uppercase">Criado em</label>
                <p className="text-lg">
                  {new Date(project.created_at).toLocaleDateString('pt-BR', {
                    day: '2-digit',
                    month: 'long',
                    year: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                  })}
                </p>
              </div>
            </div>
          </div>

          {/* Dica */}
          <div className="bg-blue-50 border-2 border-blue-200 rounded-2xl p-6">
            <div className="flex items-start space-x-3">
              <span className="text-3xl">💡</span>
              <div>
                <h3 className="font-bold text-blue-900 mb-2">Dica</h3>
                <p className="text-blue-800 text-sm">
                  Clique em "Ajustar Imagem" para fazer mudanças. Por exemplo:
                  "adicionar mais gavetas", "mudar cor para branco", "tornar mais moderno", etc.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
