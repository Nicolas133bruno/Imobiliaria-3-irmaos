// Frontend Integration - Integração completa frontend-backend
class FrontendIntegration {
    constructor() {
        this.api = new ImobiliariaAPI();
        this.isApiAvailable = false;
        this.properties = [];
        this.stats = {};
        this.loadingStates = new Set();
        this.retryCount = 0;
        this.maxRetries = 3;
    }

    async init() {
        console.log('Inicializando integração frontend...');
        
        // Testar conexão com API
        await this.testApiConnection();
        
        if (this.isApiAvailable) {
            // Carregar dados dinâmicos da API
            await this.loadDynamicData();
            
            // Atualizar interface com dados reais
            this.updateInterfaceWithRealData();
            
            // Configurar event listeners
            this.bindEvents();
            
            console.log('Integração frontend inicializada com sucesso');
        } else {
            console.warn('API não disponível. Usando dados estáticos.');
            this.useFallbackData();
        }
    }

    async testApiConnection() {
        try {
            this.showLoading('api-test');
            
            // Testar endpoint de health check
            const healthResponse = await this.api.get('/health');
            
            if (healthResponse && healthResponse.status === 'ok') {
                this.isApiAvailable = true;
                this.retryCount = 0;
                console.log('✅ API conectada com sucesso');
            } else {
                throw new Error('Health check falhou');
            }
            
        } catch (error) {
            console.warn('❌ Falha na conexão com API:', error.message);
            
            // Tentar reconexão
            if (this.retryCount < this.maxRetries) {
                this.retryCount++;
                console.log(`Tentativa ${this.retryCount} de ${this.maxRetries}...`);
                
                // Aguardar antes de tentar novamente (exponencial backoff)
                await this.delay(1000 * this.retryCount);
                await this.testApiConnection();
            } else {
                this.isApiAvailable = false;
            }
        } finally {
            this.hideLoading('api-test');
        }
    }

    async loadDynamicData() {
        if (!this.isApiAvailable) return;

        try {
            this.showLoading('data-loading');
            
            // Carregar propriedades
            const propertiesResponse = await this.api.get('/properties?limit=6&status=available');
            this.properties = propertiesResponse.data || [];
            
            // Carregar estatísticas
            const statsResponse = await this.api.get('/statistics');
            this.stats = statsResponse.data || {};
            
            console.log('📊 Dados carregados:', {
                properties: this.properties.length,
                stats: this.stats
            });
            
        } catch (error) {
            console.error('Erro ao carregar dados:', error);
            this.properties = [];
            this.stats = {};
        } finally {
            this.hideLoading('data-loading');
        }
    }

    updateInterfaceWithRealData() {
        if (this.properties.length > 0) {
            this.renderPropertyCards();
        }
        
        if (Object.keys(this.stats).length > 0) {
            this.updateStatistics();
        }
        
        this.updateFeaturedContent();
    }

    renderPropertyCards() {
        const propertiesContainer = document.querySelector('.properties .row');
        if (!propertiesContainer) return;

        // Limpar conteúdo estático
        propertiesContainer.innerHTML = '';

        // Renderizar cards com dados reais
        this.properties.forEach(property => {
            const propertyCard = this.createPropertyCard(property);
            propertiesContainer.appendChild(propertyCard);
        });

        console.log(`🏠 ${this.properties.length} propriedades renderizadas`);
    }

    createPropertyCard(property) {
        const colDiv = document.createElement('div');
        colDiv.className = 'col-lg-4 col-md-6';
        
        colDiv.innerHTML = `
            <div class="item">
                <a href="property-details.html?id=${property.id}">
                    <img src="${property.image_url || 'assets/images/property-01.jpg'}" 
                         alt="${property.title}" 
                         onerror="this.src='assets/images/property-01.jpg'">
                </a>
                <span class="category">${property.type || 'Luxury Villa'}</span>
                <h6>${this.formatCurrency(property.price)}</h6>
                <h4><a href="property-details.html?id=${property.id}">${property.address}</a></h4>
                <ul>
                    <li>Quartos: <span>${property.bedrooms || 'N/A'}</span></li>
                    <li>Banheiros: <span>${property.bathrooms || 'N/A'}</span></li>
                    <li>Área: <span>${property.area ? property.area + 'm²' : 'N/A'}</span></li>
                    <li>Andar: <span>${property.floor || 'N/A'}</span></li>
                    <li>Estacionamento: <span>${property.parking || 'N/A'}</span></li>
                </ul>
                <div class="main-button">
                    <a href="property-details.html?id=${property.id}">Agendar visita</a>
                </div>
            </div>
        `;
        
        return colDiv;
    }

    updateStatistics() {
        // Atualizar contadores na página inicial
        const counters = {
            'properties-count': this.stats.total_properties || 0,
            'happy-customers': this.stats.total_customers || 0,
            'awards-count': this.stats.awards || 0,
            'years-count': this.stats.years_experience || 0
        };

        Object.keys(counters).forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.textContent = counters[id];
            }
        });

        console.log('📈 Estatísticas atualizadas:', counters);
    }

    updateFeaturedContent() {
        // Atualizar conteúdo em destaque com dados reais
        if (this.properties.length > 0) {
            const featuredProperty = this.properties[0];
            
            // Atualizar banner principal se existir
            const mainBanner = document.querySelector('.main-banner h2');
            if (mainBanner) {
                mainBanner.textContent = featuredProperty.title || 'Encontre Sua Casa dos Sonhos';
            }
            
            // Atualizar texto de destaque
            const featuredText = document.querySelector('.featured-text');
            if (featuredText) {
                featuredText.innerHTML = `
                    <h6>| ${featuredProperty.type || 'Propriedade em Destaque'}</h6>
                    <h2>${featuredProperty.title}</h2>
                    <p>${featuredProperty.description || 'Descubra esta incrível oportunidade imobiliária.'}</p>
                `;
            }
        }
    }

    bindEvents() {
        // Bind de eventos para formulários
        this.bindFormEvents();
        
        // Bind de eventos para agendamentos
        this.bindScheduleEvents();
        
        // Bind de eventos para navegação
        this.bindNavigationEvents();
    }

    bindFormEvents() {
        const contactForm = document.getElementById('contact-form');
        if (contactForm) {
            contactForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                await this.handleContactForm(e.target);
            });
        }
    }

    async handleContactForm(form) {
        try {
            this.showLoading('form-submit');
            
            const formData = new FormData(form);
            const data = Object.fromEntries(formData.entries());
            
            if (this.isApiAvailable) {
                await this.api.post('/contacts', data);
                this.showSuccess('Mensagem enviada com sucesso! Entraremos em contato em breve.');
                form.reset();
            } else {
                this.showSuccess('Mensagem preparada para envio. Entraremos em contato quando a conexão for restabelecida.');
                // Aqui você pode armazenar localmente para envio posterior
            }
            
        } catch (error) {
            this.showError('Erro ao enviar mensagem. Tente novamente.');
            console.error('Form error:', error);
        } finally {
            this.hideLoading('form-submit');
        }
    }

    bindScheduleEvents() {
        // Adicionar eventos para todos os botões de agendamento
        document.addEventListener('click', (e) => {
            if (e.target.closest('.main-button a') || e.target.closest('.icon-button a')) {
                const href = e.target.closest('a').getAttribute('href');
                if (href && href.includes('property-details.html')) {
                    e.preventDefault();
                    this.handleScheduleClick(href);
                }
            }
        });
    }

    handleScheduleClick(href) {
        // Extrair ID da propriedade da URL
        const urlParams = new URLSearchParams(href.split('?')[1]);
        const propertyId = urlParams.get('id');
        
        if (propertyId && this.isApiAvailable) {
            // Redirecionar para página de detalhes
            window.location.href = `property-details.html?id=${propertyId}`;
        } else {
            // Fallback para página estática
            window.location.href = 'property-details.html';
        }
    }

    bindNavigationEvents() {
        // Adicionar admin link se usuário estiver logado
        this.addAdminLink();
    }

    addAdminLink() {
        // Verificar se usuário está logado (simplificado)
        const token = localStorage.getItem('auth_token');
        if (token) {
            const headerNav = document.querySelector('.main-nav');
            if (headerNav) {
                const adminLink = document.createElement('li');
                adminLink.className = 'scroll-to-section';
                adminLink.innerHTML = '<a href="admin.html">Admin</a>';
                headerNav.appendChild(adminLink);
            }
        }
    }

    useFallbackData() {
        // Dados fallback para quando API não está disponível
        this.properties = this.getFallbackProperties();
        this.stats = this.getFallbackStats();
        
        this.updateInterfaceWithRealData();
    }

    getFallbackProperties() {
        return [
            {
                id: 1,
                title: 'Residência Luxury Miami',
                type: 'Luxury Villa',
                price: 2264000,
                address: '18 New Street Miami, OR 97219',
                bedrooms: 8,
                bathrooms: 8,
                area: 545,
                floor: 3,
                parking: '6 vagas',
                image_url: 'assets/images/property-01.jpg'
            },
            // ... mais propriedades fallback
        ];
    }

    getFallbackStats() {
        return {
            total_properties: 150,
            total_customers: 250,
            awards: 15,
            years_experience: 10
        };
    }

    // Utilitários
    formatCurrency(amount) {
        return new Intl.NumberFormat('pt-BR', {
            style: 'currency',
            currency: 'BRL'
        }).format(amount);
    }

    showLoading(id) {
        this.loadingStates.add(id);
        document.body.style.cursor = 'wait';
    }

    hideLoading(id) {
        this.loadingStates.delete(id);
        if (this.loadingStates.size === 0) {
            document.body.style.cursor = 'default';
        }
    }

    showSuccess(message) {
        this.showToast(message, 'success');
    }

    showError(message) {
        this.showToast(message, 'error');
    }

    showToast(message, type = 'info') {
        // Implementação simples de toast notification
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        toast.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 20px;
            background: ${type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'};
            color: white;
            border-radius: 5px;
            z-index: 10000;
            max-width: 300px;
        `;
        toast.textContent = message;
        
        document.body.appendChild(toast);
        
        setTimeout(() => {
            toast.remove();
        }, 5000);
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Inicialização automática quando o script é carregado
document.addEventListener('DOMContentLoaded', function() {
    window.frontendIntegration = new FrontendIntegration();
    window.frontendIntegration.init();
});