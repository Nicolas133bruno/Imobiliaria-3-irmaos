// Configurações da API para integração frontend-backend
class ApiConfig {
    static get BASE_URL() {
        // URL base da API - ajuste conforme necessário
        return 'http://localhost:3000/api';
    }

    static get ENDPOINTS() {
        return {
            PROPERTIES: '/properties',
            PROPERTY_DETAILS: '/properties', // /:id
            USERS: '/users',
            BROKERS: '/brokers',
            VISITS: '/visits',
            CONTRACTS: '/contracts',
            STATISTICS: '/statistics',
            AUTH: '/auth'
        };
    }

    static get DEFAULT_HEADERS() {
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        };
    }

    static get TIMEOUT() {
        return 10000; // 10 segundos
    }

    // Método para construir URL completa
    static buildUrl(endpoint, params = {}) {
        let url = `${this.BASE_URL}${endpoint}`;
        
        // Substituir parâmetros na URL (ex: /properties/:id)
        Object.keys(params).forEach(key => {
            if (url.includes(`:${key}`)) {
                url = url.replace(`:${key}`, params[key]);
                delete params[key];
            }
        });

        // Adicionar query parameters se houver
        const queryParams = new URLSearchParams(params);
        if (queryParams.toString()) {
            url += `?${queryParams.toString()}`;
        }

        return url;
    }

    // Método para tratamento de erros padrão
    static handleError(error) {
        console.error('API Error:', error);
        
        if (error.response) {
            // Erro da API com resposta
            const status = error.response.status;
            const message = error.response.data?.message || 'Erro desconhecido';
            
            switch (status) {
                case 400:
                    throw new Error(`Requisição inválida: ${message}`);
                case 401:
                    throw new Error('Não autorizado. Faça login novamente.');
                case 403:
                    throw new Error('Acesso negado.');
                case 404:
                    throw new Error('Recurso não encontrado.');
                case 500:
                    throw new Error('Erro interno do servidor.');
                default:
                    throw new Error(`Erro ${status}: ${message}`);
            }
        } else if (error.request) {
            // Erro de rede
            throw new Error('Erro de conexão. Verifique sua internet.');
        } else {
            // Outros erros
            throw new Error(error.message || 'Erro desconhecido');
        }
    }

    // Método para verificar se a API está disponível
    static async checkApiStatus() {
        try {
            const response = await fetch(`${this.BASE_URL}/health`, {
                method: 'GET',
                headers: this.DEFAULT_HEADERS,
                timeout: this.TIMEOUT
            });
            
            return response.ok;
        } catch (error) {
            console.warn('API status check failed:', error);
            return false;
        }
    }
}

// Exportar para uso global
window.ApiConfig = ApiConfig;