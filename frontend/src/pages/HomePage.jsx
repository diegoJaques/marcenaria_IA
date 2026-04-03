import { Link } from 'react-router-dom'

export default function HomePage() {
  return (
    <div className="text-center">
      {/* Hero Section - BEM SIMPLES */}
      <div className="bg-white rounded-3xl shadow-xl p-8 md:p-12 mb-8">
        <div className="text-6xl mb-6">🪵✨</div>
        <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">
          Bem-vindo ao MarcenAI!
        </h2>
        <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Crie imagens incríveis dos seus projetos de marcenaria usando Inteligência Artificial.
          <br />
          <strong className="text-wood-700">É fácil e rápido!</strong>
        </p>

        {/* Botão Principal GIGANTE */}
        <Link
          to="/new"
          className="inline-block bg-wood-600 hover:bg-wood-700 text-white font-bold py-6 px-12 rounded-2xl shadow-2xl transition-all duration-200 text-2xl hover:scale-105"
        >
          <span className="text-3xl mr-3">➕</span>
          Criar Novo Projeto
        </Link>
      </div>

      {/* Como Funciona - COM ÍCONES GRANDES */}
      <div className="bg-white rounded-3xl shadow-xl p-8 md:p-12 mb-8">
        <h3 className="text-2xl md:text-3xl font-bold text-gray-900 mb-8">
          Como Funciona?
        </h3>

        <div className="grid md:grid-cols-3 gap-8 text-left">
          {/* Passo 1 */}
          <div className="flex flex-col items-center text-center">
            <div className="text-6xl mb-4">📝</div>
            <div className="bg-wood-600 text-white rounded-full w-12 h-12 flex items-center justify-center font-bold text-xl mb-3">
              1
            </div>
            <h4 className="font-bold text-lg mb-2">Responda Perguntas Simples</h4>
            <p className="text-gray-600">
              Que móvel? Para qual ambiente? Qual estilo? Tudo com ícones fáceis!
            </p>
          </div>

          {/* Passo 2 */}
          <div className="flex flex-col items-center text-center">
            <div className="text-6xl mb-4">🤖</div>
            <div className="bg-wood-600 text-white rounded-full w-12 h-12 flex items-center justify-center font-bold text-xl mb-3">
              2
            </div>
            <h4 className="font-bold text-lg mb-2">A IA Faz a Mágica</h4>
            <p className="text-gray-600">
              Nosso sistema cria imagens profissionais automaticamente. Você não precisa fazer nada!
            </p>
          </div>

          {/* Passo 3 */}
          <div className="flex flex-col items-center text-center">
            <div className="text-6xl mb-4">🎨</div>
            <div className="bg-wood-600 text-white rounded-full w-12 h-12 flex items-center justify-center font-bold text-xl mb-3">
              3
            </div>
            <h4 className="font-bold text-lg mb-2">Mostre ao Cliente</h4>
            <p className="text-gray-600">
              Receba imagens realistas para mostrar como ficará o móvel. Se quiser ajustar, é só pedir!
            </p>
          </div>
        </div>
      </div>

      {/* Botões de Ação */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Criar Projeto */}
        <Link
          to="/new"
          className="option-card hover:scale-105 transform transition"
        >
          <div className="text-center">
            <div className="text-6xl mb-4">✨</div>
            <h3 className="text-xl font-bold mb-2">Criar Novo Projeto</h3>
            <p className="text-gray-600">
              Comece um projeto do zero com a ajuda da IA
            </p>
          </div>
        </Link>

        {/* Ver Projetos */}
        <Link
          to="/projects"
          className="option-card hover:scale-105 transform transition"
        >
          <div className="text-center">
            <div className="text-6xl mb-4">📚</div>
            <h3 className="text-xl font-bold mb-2">Meus Projetos</h3>
            <p className="text-gray-600">
              Veja todos os projetos que você já criou
            </p>
          </div>
        </Link>
      </div>

      {/* Dica */}
      <div className="mt-8 bg-blue-50 border-2 border-blue-200 rounded-2xl p-6">
        <div className="flex items-start space-x-4">
          <div className="text-4xl">💡</div>
          <div className="text-left">
            <h4 className="font-bold text-blue-900 mb-2">Dica!</h4>
            <p className="text-blue-800">
              Quanto mais detalhes você fornecer (cores, materiais, tamanho), melhor ficará a imagem criada pela IA!
            </p>
          </div>
        </div>
      </div>
    </div>
  )
}
