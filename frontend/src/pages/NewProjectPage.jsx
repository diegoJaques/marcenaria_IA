import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { createProject } from '../services/api'

// Opções com ÍCONES e nomes simples
const FURNITURE_OPTIONS = [
  { value: 'cadeira', label: 'Cadeira', icon: '🪑' },
  { value: 'sofa', label: 'Sofá', icon: '🛋️' },
  { value: 'armario', label: 'Armário', icon: '🚪' },
  { value: 'estante', label: 'Estante', icon: '📚' },
  { value: 'mesa', label: 'Mesa', icon: '🍽️' },
  { value: 'bancada', label: 'Bancada', icon: '🔨' },
  { value: 'cama', label: 'Cama', icon: '🛏️' },
  { value: 'criado', label: 'Criado-mudo', icon: '📦' },
  { value: 'outro', label: 'Outro', icon: '💡' },
]

const ROOM_OPTIONS = [
  { value: 'cozinha', label: 'Cozinha', icon: '🍳' },
  { value: 'sala', label: 'Sala', icon: '🛋️' },
  { value: 'quarto', label: 'Quarto', icon: '🛏️' },
  { value: 'banheiro', label: 'Banheiro', icon: '🚿' },
  { value: 'escritorio', label: 'Escritório', icon: '💼' },
  { value: 'area_externa', label: 'Área Externa', icon: '🌳' },
  { value: 'lavanderia', label: 'Lavanderia', icon: '🧺' },
  { value: 'garagem', label: 'Garagem', icon: '🚗' },
]

const STYLE_OPTIONS = [
  { value: 'moderno', label: 'Moderno', icon: '✨', desc: 'Limpo e minimalista' },
  { value: 'rustico', label: 'Rústico', icon: '🌲', desc: 'Madeira natural' },
  { value: 'industrial', label: 'Industrial', icon: '🏭', desc: 'Metal e madeira' },
  { value: 'classico', label: 'Clássico', icon: '👑', desc: 'Tradicional e elegante' },
  { value: 'contemporaneo', label: 'Contemporâneo', icon: '🎨', desc: 'Atual e sofisticado' },
  { value: 'provencal', label: 'Provençal', icon: '🌸', desc: 'Romântico e vintage' },
]

export default function NewProjectPage() {
  const navigate = useNavigate()
  const [step, setStep] = useState(1)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const [formData, setFormData] = useState({
    furniture_type: '',
    room: '',
    style: '',
    size: '',
    // Novos campos para móveis planejados
    width_cm: '',
    height_cm: '',
    depth_cm: '',
    reference_image_url: '',
    material: '',
    color: '',
    special_features: '',
    client_name: '',
    client_notes: '',
  })

  const [uploadingImage, setUploadingImage] = useState(false)
  const [imagePreview, setImagePreview] = useState(null)

  const handleSelect = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }))
  }

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }))
  }

  const canGoNext = () => {
    if (step === 1) return formData.furniture_type
    if (step === 2) return formData.room
    if (step === 3) return formData.style
    return true
  }

  const handleNext = () => {
    if (canGoNext()) {
      setStep(step + 1)
      window.scrollTo(0, 0)
    }
  }

  const handleBack = () => {
    setStep(step - 1)
    window.scrollTo(0, 0)
  }

  const handleImageUpload = async (e) => {
    const file = e.target.files[0]
    if (!file) return

    // Validar tipo
    if (!file.type.startsWith('image/')) {
      setError('Por favor, selecione uma imagem válida')
      return
    }

    // Validar tamanho (10MB)
    if (file.size > 10 * 1024 * 1024) {
      setError('Imagem muito grande. Máximo: 10MB')
      return
    }

    setUploadingImage(true)
    setError(null)

    try {
      // Preview local
      const reader = new FileReader()
      reader.onloadend = () => {
        setImagePreview(reader.result)
      }
      reader.readAsDataURL(file)

      // Upload para o servidor
      const formData = new FormData()
      formData.append('file', file)

      const response = await fetch('http://localhost:8000/api/projects/upload-reference', {
        method: 'POST',
        body: formData,
      })

      if (!response.ok) {
        throw new Error('Erro ao fazer upload da imagem')
      }

      const data = await response.json()

      // Salvar URL da imagem no formData
      setFormData(prev => ({
        ...prev,
        reference_image_url: data.reference_image_url
      }))

      console.log('✅ Imagem enviada:', data.reference_image_url)
    } catch (err) {
      setError('Erro ao enviar imagem. Tente novamente.')
      console.error(err)
      setImagePreview(null)
    } finally {
      setUploadingImage(false)
    }
  }

  const handleSubmit = async () => {
    setLoading(true)
    setError(null)

    try {
      // Preparar dados com conversão de números
      const projectData = {
        ...formData,
        width_cm: formData.width_cm ? parseFloat(formData.width_cm) : null,
        height_cm: formData.height_cm ? parseFloat(formData.height_cm) : null,
        depth_cm: formData.depth_cm ? parseFloat(formData.depth_cm) : null,
      }

      const project = await createProject(projectData)
      navigate(`/projects/${project.id}`)
    } catch (err) {
      setError('Erro ao criar projeto. Verifique sua conexão e tente novamente.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto">
      {/* Progresso */}
      <div className="bg-white rounded-2xl shadow-lg p-6 mb-6">
        <div className="flex items-center justify-between mb-4">
          <span className="text-sm font-semibold text-gray-600">
            Passo {step} de 5
          </span>
          <span className="text-sm text-gray-500">
            {Math.round((step / 5) * 100)}% completo
          </span>
        </div>
        <div className="w-full bg-gray-200 rounded-full h-3">
          <div
            className="bg-wood-600 h-3 rounded-full transition-all duration-300"
            style={{ width: `${(step / 5) * 100}%` }}
          />
        </div>
      </div>

      {/* Conteúdo do Passo */}
      <div className="bg-white rounded-2xl shadow-xl p-8">
        {/* PASSO 1: Tipo de Móvel */}
        {step === 1 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-3 text-center">
              Que móvel você quer criar?
            </h2>
            <p className="text-gray-600 mb-8 text-center">
              Escolha uma opção abaixo
            </p>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              {FURNITURE_OPTIONS.map(option => (
                <button
                  key={option.value}
                  onClick={() => handleSelect('furniture_type', option.value)}
                  className={`option-card ${formData.furniture_type === option.value ? 'selected' : ''}`}
                >
                  <div className="text-5xl mb-2">{option.icon}</div>
                  <div className="font-semibold">{option.label}</div>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* PASSO 2: Ambiente */}
        {step === 2 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-3 text-center">
              Para qual ambiente?
            </h2>
            <p className="text-gray-600 mb-8 text-center">
              Onde ficará o móvel?
            </p>

            <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
              {ROOM_OPTIONS.map(option => (
                <button
                  key={option.value}
                  onClick={() => handleSelect('room', option.value)}
                  className={`option-card ${formData.room === option.value ? 'selected' : ''}`}
                >
                  <div className="text-5xl mb-2">{option.icon}</div>
                  <div className="font-semibold">{option.label}</div>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* PASSO 3: Estilo */}
        {step === 3 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-3 text-center">
              Qual estilo você prefere?
            </h2>
            <p className="text-gray-600 mb-8 text-center">
              Escolha o visual do móvel
            </p>

            <div className="grid md:grid-cols-2 gap-4">
              {STYLE_OPTIONS.map(option => (
                <button
                  key={option.value}
                  onClick={() => handleSelect('style', option.value)}
                  className={`option-card text-left ${formData.style === option.value ? 'selected' : ''}`}
                >
                  <div className="flex items-center space-x-4">
                    <div className="text-5xl">{option.icon}</div>
                    <div>
                      <div className="font-bold text-lg">{option.label}</div>
                      <div className="text-sm text-gray-600">{option.desc}</div>
                    </div>
                  </div>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* PASSO 4: Medidas e Referência (Móveis Planejados) */}
        {step === 4 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-3 text-center">
              📏 Móvel Planejado Sob Medida
            </h2>
            <p className="text-gray-600 mb-8 text-center">
              Informe as medidas exatas e/ou envie uma foto de referência
            </p>

            <div className="space-y-6">
              {/* Medidas Exatas */}
              <div className="bg-blue-50 border-2 border-blue-200 rounded-xl p-6">
                <h3 className="text-xl font-bold mb-4 text-blue-900">
                  🎯 Medidas Exatas (em centímetros)
                </h3>
                <p className="text-sm text-blue-700 mb-4">
                  Deixe em branco se não souber as medidas exatas
                </p>

                <div className="grid md:grid-cols-3 gap-4">
                  <div>
                    <label className="block text-sm font-semibold mb-2 text-gray-700">
                      Largura (cm)
                    </label>
                    <input
                      type="number"
                      step="0.1"
                      value={formData.width_cm}
                      onChange={(e) => handleInputChange('width_cm', e.target.value)}
                      placeholder="Ex: 180"
                      className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold mb-2 text-gray-700">
                      Altura (cm)
                    </label>
                    <input
                      type="number"
                      step="0.1"
                      value={formData.height_cm}
                      onChange={(e) => handleInputChange('height_cm', e.target.value)}
                      placeholder="Ex: 220"
                      className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold mb-2 text-gray-700">
                      Profundidade (cm)
                    </label>
                    <input
                      type="number"
                      step="0.1"
                      value={formData.depth_cm}
                      onChange={(e) => handleInputChange('depth_cm', e.target.value)}
                      placeholder="Ex: 45"
                      className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                    />
                  </div>
                </div>
              </div>

              {/* Upload de Imagem de Referência */}
              <div className="bg-purple-50 border-2 border-purple-200 rounded-xl p-6">
                <h3 className="text-xl font-bold mb-4 text-purple-900">
                  📸 Imagem de Referência
                </h3>
                <p className="text-sm text-purple-700 mb-4">
                  Envie uma foto de exemplo do que você quer criar
                </p>

                <div className="flex flex-col items-center">
                  {/* Preview da Imagem */}
                  {imagePreview && (
                    <div className="mb-4 relative">
                      <img
                        src={imagePreview}
                        alt="Preview"
                        className="max-w-full max-h-64 rounded-xl shadow-lg"
                      />
                      <button
                        onClick={() => {
                          setImagePreview(null)
                          setFormData(prev => ({ ...prev, reference_image_url: '' }))
                        }}
                        className="absolute top-2 right-2 bg-red-500 text-white rounded-full w-8 h-8 flex items-center justify-center hover:bg-red-600"
                      >
                        ✕
                      </button>
                    </div>
                  )}

                  {/* Botão de Upload */}
                  <label className={`
                    cursor-pointer bg-purple-600 text-white px-6 py-3 rounded-xl
                    font-semibold hover:bg-purple-700 transition
                    ${uploadingImage ? 'opacity-50 cursor-not-allowed' : ''}
                  `}>
                    {uploadingImage ? (
                      <>
                        <span className="spinner w-5 h-5 inline-block mr-2"></span>
                        Enviando...
                      </>
                    ) : imagePreview ? (
                      '🔄 Trocar Imagem'
                    ) : (
                      '📤 Escolher Imagem'
                    )}
                    <input
                      type="file"
                      accept="image/*"
                      onChange={handleImageUpload}
                      disabled={uploadingImage}
                      className="hidden"
                    />
                  </label>

                  <p className="text-xs text-gray-500 mt-2">
                    Formatos: JPG, PNG, WEBP (máx. 10MB)
                  </p>
                </div>
              </div>

              <div className="bg-yellow-50 border-2 border-yellow-200 rounded-xl p-4">
                <p className="text-sm text-yellow-800">
                  💡 <strong>Dica:</strong> Quanto mais detalhes você fornecer (medidas + foto de referência),
                  mais preciso ficará o projeto gerado pela IA!
                </p>
              </div>
            </div>
          </div>
        )}

        {/* PASSO 5: Detalhes Extras (Opcional) */}
        {step === 5 && (
          <div>
            <h2 className="text-3xl font-bold text-gray-900 mb-3 text-center">
              Mais Detalhes (Opcional)
            </h2>
            <p className="text-gray-600 mb-8 text-center">
              Quanto mais detalhes, melhor fica a imagem! Mas pode pular se quiser.
            </p>

            <div className="space-y-6">
              {/* Tamanho */}
              <div>
                <label className="block text-lg font-semibold mb-3">
                  Tamanho
                </label>
                <div className="grid grid-cols-3 gap-3">
                  {['pequeno', 'médio', 'grande'].map(size => (
                    <button
                      key={size}
                      onClick={() => handleSelect('size', size)}
                      className={`py-3 px-4 rounded-xl font-semibold transition ${
                        formData.size === size
                          ? 'bg-wood-600 text-white'
                          : 'bg-gray-100 hover:bg-gray-200'
                      }`}
                    >
                      {size.charAt(0).toUpperCase() + size.slice(1)}
                    </button>
                  ))}
                </div>
              </div>

              {/* Material */}
              <div>
                <label className="block text-lg font-semibold mb-2">
                  Material (ex: MDF, madeira de lei, pinus)
                </label>
                <input
                  type="text"
                  value={formData.material}
                  onChange={(e) => handleInputChange('material', e.target.value)}
                  placeholder="Digite o material..."
                  className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                />
              </div>

              {/* Cor */}
              <div>
                <label className="block text-lg font-semibold mb-2">
                  Cor (ex: branco, natural, preto)
                </label>
                <input
                  type="text"
                  value={formData.color}
                  onChange={(e) => handleInputChange('color', e.target.value)}
                  placeholder="Digite a cor..."
                  className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                />
              </div>

              {/* Características Especiais */}
              <div>
                <label className="block text-lg font-semibold mb-2">
                  Características Especiais (ex: 3 gavetas, portas de vidro)
                </label>
                <textarea
                  value={formData.special_features}
                  onChange={(e) => handleInputChange('special_features', e.target.value)}
                  placeholder="Descreva características especiais..."
                  rows="3"
                  className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                />
              </div>

              {/* Nome do Cliente */}
              <div>
                <label className="block text-lg font-semibold mb-2">
                  Nome do Cliente (opcional)
                </label>
                <input
                  type="text"
                  value={formData.client_name}
                  onChange={(e) => handleInputChange('client_name', e.target.value)}
                  placeholder="Para quem é esse projeto?"
                  className="w-full px-4 py-3 border-2 border-gray-300 rounded-xl focus:border-wood-500 focus:outline-none text-lg"
                />
              </div>
            </div>
          </div>
        )}

        {/* Erro */}
        {error && (
          <div className="mt-6 bg-red-50 border-2 border-red-300 rounded-xl p-4 text-red-800">
            <strong>❌ Ops!</strong> {error}
          </div>
        )}

        {/* Botões de Navegação */}
        <div className="flex justify-between mt-8 pt-6 border-t">
          <button
            onClick={handleBack}
            disabled={step === 1}
            className={`btn-secondary ${step === 1 ? 'opacity-50 cursor-not-allowed' : ''}`}
          >
            ← Voltar
          </button>

          {step < 5 ? (
            <button
              onClick={handleNext}
              disabled={!canGoNext()}
              className={`btn-primary ${!canGoNext() ? 'opacity-50 cursor-not-allowed' : ''}`}
            >
              Próximo →
            </button>
          ) : (
            <button
              onClick={handleSubmit}
              disabled={loading}
              className="btn-primary relative"
            >
              {loading ? (
                <>
                  <span className="spinner w-6 h-6 inline-block mr-2"></span>
                  Criando mágica...
                </>
              ) : (
                <>
                  ✨ Criar Projeto
                </>
              )}
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
