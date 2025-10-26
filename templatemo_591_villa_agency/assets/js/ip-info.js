async function buscarInfos() {
 try {
    const requisicao = await fetch("https://ipinfo.io/json");
    
    if (!requisicao.ok) {
        throw new Error(`Erro HTTP: ${requisicao.status}`);
    }
    
    const respostaEmJSON = await requisicao.json();
    
    // Exibir informações de localização do visitante
    exibirInformacoesVisitante(respostaEmJSON);
    
    // Log para debug
    console.log("Informações do visitante:", respostaEmJSON);
    
 } catch (error) {
  console.log( "Erro ao buscar informações:", error);
  // Exibir mensagem de erro amigável
  exibirMensagemErro();
 }
}

function exibirInformacoesVisitante(dados) {
    // Criar elemento para mostrar as informações
    const infoContainer = document.createElement('div');
    infoContainer.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 15px;
        border-radius: 8px;
        font-size: 14px;
        z-index: 1000;
        max-width: 300px;
        backdrop-filter: blur(10px);
    `;
    
    infoContainer.innerHTML = `
        <h4 style="margin: 0 0 10px 0; color: #f5a425;">📍 Localização Detectada</h4>
        <p style="margin: 5px 0;"><strong>País:</strong> ${dados.country || 'N/A'}</p>
        <p style="margin: 5px 0;"><strong>Região:</strong> ${dados.region || 'N/A'}</p>
        <p style="margin: 5px 0;"><strong>Cidade:</strong> ${dados.city || 'N/A'}</p>
        <p style="margin: 5px 0;"><strong>Provedor:</strong> ${dados.org || 'N/A'}</p>
        <button onclick="this.parentElement.remove()" style="
            background: #f5a425;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            color: white;
            cursor: pointer;
            margin-top: 10px;
        ">Fechar</button>
    `;
    
    document.body.appendChild(infoContainer);
    
    // Remover automaticamente após 15 segundos
    setTimeout(() => {
        if (infoContainer.parentElement) {
            infoContainer.remove();
        }
    }, 15000);
}

function exibirMensagemErro() {
    const errorContainer = document.createElement('div');
    errorContainer.style.cssText = `
        position: fixed;
        bottom: 20px;
        right: 20px;
        background: rgba(255, 0, 0, 0.8);
        color: white;
        padding: 15px;
        border-radius: 8px;
        font-size: 14px;
        z-index: 1000;
        max-width: 300px;
    `;
    
    errorContainer.innerHTML = `
        <h4 style="margin: 0 0 10px 0;">⚠️ Erro de Conexão</h4>
        <p style="margin: 5px 0;">Não foi possível detectar sua localização.</p>
        <button onclick="this.parentElement.remove()" style="
            background: white;
            border: none;
            padding: 5px 10px;
            border-radius: 4px;
            color: #ff0000;
            cursor: pointer;
            margin-top: 10px;
        ">Fechar</button>
    `;
    
    document.body.appendChild(errorContainer);
}

// Executar a função quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    buscarInfos();
});
