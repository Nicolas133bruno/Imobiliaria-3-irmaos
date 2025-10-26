// API Integration for Imobiliaria 3 Irmãos
const API_BASE_URL = 'http://localhost:8000';

class ImobiliariaAPI {
    constructor() {
        this.baseUrl = API_BASE_URL;
    }

    async request(endpoint, options = {}) {
        try {
            const response = await fetch(`${this.baseUrl}${endpoint}`, {
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                },
                ...options
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            return await response.json();
        } catch (error) {
            console.error('API Request failed:', error);
            throw error;
        }
    }

    // Usuários
    async getUsuarios() {
        return await this.request('/usuarios/');
    }

    async createUsuario(usuario) {
        return await this.request('/usuarios/', {
            method: 'POST',
            body: JSON.stringify(usuario)
        });
    }

    async updateUsuario(id, usuario) {
        return await this.request(`/usuarios/${id}`, {
            method: 'PUT',
            body: JSON.stringify(usuario)
        });
    }

    async deleteUsuario(id) {
        return await this.request(`/usuarios/${id}`, {
            method: 'DELETE'
        });
    }

    // Imóveis
    async getImoveis() {
        return await this.request('/imoveis/');
    }

    async getImovel(id) {
        return await this.request(`/imoveis/${id}`);
    }

    async createImovel(imovel) {
        return await this.request('/imoveis/', {
            method: 'POST',
            body: JSON.stringify(imovel)
        });
    }

    async updateImovel(id, imovel) {
        return await this.request(`/imoveis/${id}`, {
            method: 'PUT',
            body: JSON.stringify(imovel)
        });
    }

    async deleteImovel(id) {
        return await this.request(`/imoveis/${id}`, {
            method: 'DELETE'
        });
    }

    // Corretores
    async getCorretores() {
        return await this.request('/corretores/');
    }

    // Visitas
    async getVisitas() {
        return await this.request('/visitas/');
    }

    async createVisita(visita) {
        return await this.request('/visitas/', {
            method: 'POST',
            body: JSON.stringify(visita)
        });
    }

    // Contratos
    async getContratosAluguel() {
        return await this.request('/contratos-aluguel/');
    }

    async getContratosVenda() {
        return await this.request('/contratos-venda/');
    }

    // Relatórios
    async getRelatorios() {
        return await this.request('/relatorios/');
    }
}

// Exportar para uso global
window.ImobiliariaAPI = new ImobiliariaAPI();