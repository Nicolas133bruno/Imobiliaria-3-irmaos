// Frontend Integration for Imobiliaria 3 Irmãos
class FrontendIntegration {
    constructor() {
        this.api = window.ImobiliariaAPI;
        this.init();
    }

    async init() {
        await this.loadProperties();
        await this.updateStats();
        this.bindEvents();
    }

    async loadProperties() {
        try {
            const imoveis = await this.api.getImoveis();
            this.renderProperties(imoveis);
        } catch (error) {
            console.error('Erro ao carregar imóveis:', error);
            this.showFallbackProperties();
        }
    }

    renderProperties(imoveis) {
        const propertiesContainer = document.querySelector('.properties .row');
        if (!propertiesContainer) return;

        // Limpar conteúdo existente
        propertiesContainer.innerHTML = '';

        // Renderizar imóveis
        imoveis.slice(0, 6).forEach(imovel => {
            const propertyCard = this.createPropertyCard(imovel);
            propertiesContainer.appendChild(propertyCard);
        });
    }

    createPropertyCard(imovel) {
        const col = document.createElement('div');
        col.className = 'col-lg-4 col-md-6';

        const price = imovel.valor ? `R$ ${imovel.valor.toLocaleString('pt-BR')}` : 'Consulte';
        const area = imovel.area ? `${imovel.area}m²` : 'N/A';
        const quartos = imovel.quartos || 'N/A';
        const banheiros = imovel.banheiros || 'N/A';

        col.innerHTML = `
            <div class="item">
                <a href="property-details.html?id=${imovel.id_imovel}">
                    <img src="assets/images/property-0${Math.floor(Math.random() * 6) + 1}.jpg" alt="${imovel.titulo}">
                </a>
                <span class="category">${imovel.tipo || 'Imóvel'}</span>
                <h6>${price}</h6>
                <h4><a href="property-details.html?id=${imovel.id_imovel}">${imovel.titulo}</a></h4>
                <ul>
                    <li>Quartos: <span>${quartos}</span></li>
                    <li>Banheiros: <span>${banheiros}</span></li>
                    <li>Área: <span>${area}</span></li>
                    <li>Status: <span>${imovel.status || 'Disponível'}</span></li>
                </ul>
                <div class="main-button">
                    <a href="property-details.html?id=${imovel.id_imovel}">Agendar visita</a>
                </div>
            </div>
        `;

        return col;
    }

    showFallbackProperties() {
        console.log('Usando propriedades de fallback');
        // Manter o conteúdo original se a API falhar
    }

    async updateStats() {
        try {
            const [imoveis, usuarios, visitas] = await Promise.all([
                this.api.getImoveis(),
                this.api.getUsuarios(),
                this.api.getVisitas()
            ]);

            this.updateCounter('building-counter', imoveis.length);
            this.updateCounter('experience-counter', new Date().getFullYear() - 2010); // Desde 2010
            this.updateCounter('awards-counter', visitas.length);

        } catch (error) {
            console.error('Erro ao atualizar estatísticas:', error);
        }
    }

    updateCounter(elementId, value) {
        const element = document.getElementById(elementId);
        if (element) {
            element.textContent = value;
            element.setAttribute('data-to', value);
        }
    }

    bindEvents() {
        // Evento para agendamento de visitas
        document.addEventListener('click', (e) => {
            if (e.target.closest('.main-button a')) {
                e.preventDefault();
                const link = e.target.closest('a');
                const url = new URL(link.href);
                const imovelId = url.searchParams.get('id');
                
                if (imovelId) {
                    this.scheduleVisit(imovelId);
                } else {
                    window.location.href = link.href;
                }
            }
        });

        // Link para painel administrativo
        this.addAdminLink();
    }

    addAdminLink() {
        const header = document.querySelector('.header-area');
        if (header) {
            const adminLink = document.createElement('li');
            adminLink.innerHTML = '<a href="admin.html"><i class="fas fa-cog"></i> Admin</a>';
            
            const nav = header.querySelector('.nav');
            if (nav) {
                nav.appendChild(adminLink);
            }
        }
    }

    async scheduleVisit(imovelId) {
        try {
            const imovel = await this.api.getImovel(imovelId);
            
            const nome = prompt('Digite seu nome:');
            const telefone = prompt('Digite seu telefone:');
            const email = prompt('Digite seu email:');
            const data = prompt('Digite a data desejada (DD/MM/AAAA):');
            const horario = prompt('Digite o horário desejado:');

            if (nome && telefone && email && data && horario) {
                const visita = {
                    data_visita: this.formatDate(data),
                    horario_visita: horario,
                    fk_Imovel_id: imovelId,
                    nome_cliente: nome,
                    telefone_cliente: telefone,
                    email_cliente: email,
                    status_visita: 'Agendada'
                };

                await this.api.createVisita(visita);
                alert('Visita agendada com sucesso! Entraremos em contato para confirmar.');
            }
        } catch (error) {
            console.error('Erro ao agendar visita:', error);
            alert('Erro ao agendar visita. Por favor, tente novamente ou entre em contato diretamente.');
        }
    }

    formatDate(dateString) {
        const [day, month, year] = dateString.split('/');
        return `${year}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    }

    // Método para carregar detalhes do imóvel
    async loadPropertyDetails() {
        const urlParams = new URLSearchParams(window.location.search);
        const imovelId = urlParams.get('id');
        
        if (imovelId) {
            try {
                const imovel = await this.api.getImovel(imovelId);
                this.renderPropertyDetails(imovel);
            } catch (error) {
                console.error('Erro ao carregar detalhes do imóvel:', error);
            }
        }
    }

    renderPropertyDetails(imovel) {
        // Implementar renderização dos detalhes do imóvel
        console.log('Detalhes do imóvel:', imovel);
    }
}

// Inicializar integração quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    // Carregar API primeiro
    if (typeof ImobiliariaAPI !== 'undefined') {
        window.frontendIntegration = new FrontendIntegration();
    } else {
        // Tentar carregar a API se não estiver disponível
        const script = document.createElement('script');
        script.src = 'assets/js/api.js';
        script.onload = () => {
            window.frontendIntegration = new FrontendIntegration();
        };
        document.head.appendChild(script);
    }
});

// Adicionar estilos para o link admin
const adminStyles = `
    .header-area .nav li a i.fa-cog {
        margin-right: 5px;
    }
    
    @media (max-width: 768px) {
        .header-area .nav li a i.fa-cog {
            display: none;
        }
    }
`;

const styleSheet = document.createElement('style');
styleSheet.textContent = adminStyles;
document.head.appendChild(styleSheet);