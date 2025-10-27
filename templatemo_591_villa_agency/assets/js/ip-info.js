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
 }
}