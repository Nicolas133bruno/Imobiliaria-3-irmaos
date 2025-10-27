// Admin Dashboard for Imobiliaria 3 Irmãos - Sistema Profissional
class AdminDashboard {
    constructor() {
        this.api = window.ImobiliariaAPI;
        this.currentView = 'dashboard';
        this.data = {
            usuarios: [],
            imoveis: [],
            corretores: [],
            visitas: [],
            contratosAluguel: [],
            contratosVenda: []
        };
        this.init();
    }

    init() {
        this.bindEvents();
        this.setupResponsive();
        this.loadDashboard();
        this.startAutoRefresh();
    }

    bindEvents() {
        // Navegação responsiva
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const view = e.target.getAttribute('data-view');
                this.switchView(view);
            });
        });

        // Toggle sidebar em mobile
        document.querySelector('.sidebar-toggle').addEventListener('click', () => {
            this.toggleSidebar();
        });

        // Botões de ação com delegação de eventos
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-edit')) {
                this.editItem(e.target.dataset.type, e.target.dataset.id);
            } else if (e.target.classList.contains('btn-delete')) {
                this.deleteItem(e.target.dataset.type, e.target.dataset.id);
            } else if (e.target.classList.contains('btn-refresh')) {
                this.refreshData();
            } else if (e.target.classList.contains('btn-view')) {
                this.viewDetails(e.target.dataset.type, e.target.dataset.id);
            } else if (e.target.classList.contains('btn-export')) {
                this.exportData(e.target.dataset.type);
            }
        });

        // Fechar modais
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('modal') || e.target.classList.contains('btn-close-modal')) {
                this.closeModals();
            }
        });
    }

    setupResponsive() {
        // Verificar se é mobile
        if (window.innerWidth < 768) {
            document.querySelector('.admin-sidebar').classList.add('collapsed');
        }

        // Observer para mudanças de tamanho
        window.addEventListener('resize', () => {
            if (window.innerWidth < 768) {
                document.querySelector('.admin-sidebar').classList.add('collapsed');
            } else {
                document.querySelector('.admin-sidebar').classList.remove('collapsed');
            }
        });
    }

    toggleSidebar() {
        document.querySelector('.admin-sidebar').classList.toggle('collapsed');
    }

    async switchView(view) {
        this.currentView = view;
        
        // Atualizar navegação ativa
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[data-view="${view}"]`).classList.add('active');

        // Atualizar título do header
        document.querySelector('.admin-header h1').textContent = this.getViewTitle(view);

        // Mostrar loading
        this.showLoading();

        try {
            // Carregar conteúdo da view
            switch (view) {
                case 'dashboard':
                    await this.loadDashboard();
                    break;
                case 'usuarios':
                    await this.loadUsuarios();
                    break;
                case 'imoveis':
                    await this.loadImoveis();
                    break;
                case 'corretores':
                    await this.loadCorretores();
                    break;
                case 'visitas':
                    await this.loadVisitas();
                    break;
                case 'contratos':
                    await this.loadContratos();
                    break;
            }
        } catch (error) {
            this.showError('Erro ao carregar dados');
        }
    }

    getViewTitle(view) {
        const titles = {
            dashboard: 'Dashboard',
            usuarios: 'Gestão de Usuários',
            imoveis: 'Gestão de Imóveis',
            corretores: 'Gestão de Corretores',
            visitas: 'Gestão de Visitas',
            contratos: 'Gestão de Contratos'
        };
        return titles[view] || 'Painel Administrativo';
    }

    showLoading() {
        this.updateContent(`
            <div class="text-center py-5">
                <div class="spinner-border text-primary" role="status">
                    <span class="visually-hidden">Carregando...</span>
                </div>
                <p class="mt-3">Carregando dados...</p>
            </div>
        `);
    }

    async loadDashboard() {
        try {
            const [usuarios, imoveis, visitas, contratosAluguel, contratosVenda, corretores] = await Promise.all([
                this.api.getUsuarios(),
                this.api.getImoveis(),
                this.api.getVisitas(),
                this.api.getContratosAluguel(),
                this.api.getContratosVenda(),
                this.api.getCorretores()
            ]);

            // Calcular métricas avançadas
            const imoveisDisponiveis = imoveis.filter(imovel => imovel.status === 'Disponível').length;
            const imoveisVendidos = imoveis.filter(imovel => imovel.status === 'Vendido').length;
            const imoveisAlugados = imoveis.filter(imovel => imovel.status === 'Alugado').length;
            
            const visitasHoje = visitas.filter(visita => {
                const visitaDate = new Date(visita.data_visita);
                const hoje = new Date();
                return visitaDate.toDateString() === hoje.toDateString();
            }).length;

            const stats = {
                totalUsuarios: usuarios.length,
                totalImoveis: imoveis.length,
                totalVisitas: visitas.length,
                totalContratos: contratosAluguel.length + contratosVenda.length,
                totalCorretores: corretores.length,
                imoveisDisponiveis,
                imoveisVendidos,
                imoveisAlugados,
                visitasHoje,
                valorTotalContratos: contratosAluguel.reduce((sum, c) => sum + (c.valor_aluguel || 0), 0) +
                                   contratosVenda.reduce((sum, c) => sum + (c.valor_venda || 0), 0)
            };

            // Salvar dados para uso posterior
            this.data = { usuarios, imoveis, visitas, contratosAluguel, contratosVenda, corretores };

            this.renderDashboard(stats);
        } catch (error) {
            console.error('Erro no dashboard:', error);
            this.showError('Erro ao carregar dashboard. Verifique se o servidor está rodando.');
        }
    }

    async loadUsuarios() {
        try {
            const usuarios = await this.api.getUsuarios();
            this.renderUsuarios(usuarios);
        } catch (error) {
            this.showError('Erro ao carregar usuários');
        }
    }

    async loadImoveis() {
        try {
            const imoveis = await this.api.getImoveis();
            this.renderImoveis(imoveis);
        } catch (error) {
            this.showError('Erro ao carregar imóveis');
        }
    }

    async loadCorretores() {
        try {
            const corretores = await this.api.getCorretores();
            this.renderCorretores(corretores);
        } catch (error) {
            this.showError('Erro ao carregar corretores');
        }
    }

    async loadVisitas() {
        try {
            const visitas = await this.api.getVisitas();
            this.renderVisitas(visitas);
        } catch (error) {
            this.showError('Erro ao carregar visitas');
        }
    }

    async loadContratos() {
        try {
            const [aluguel, venda] = await Promise.all([
                this.api.getContratosAluguel(),
                this.api.getContratosVenda()
            ]);
            this.renderContratos(aluguel, venda);
        } catch (error) {
            this.showError('Erro ao carregar contratos');
        }
    }

    renderDashboard(stats) {
        const formatCurrency = (value) => {
            return new Intl.NumberFormat('pt-BR', {
                style: 'currency',
                currency: 'BRL'
            }).format(value);
        };

        const content = `
            <div class="row">
                <!-- Métricas Principais -->
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-primary mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.totalUsuarios}</h2>
                            <p class="card-text"><i class="fas fa-users me-2"></i>Usuários</p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-success mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.totalImoveis}</h2>
                            <p class="card-text"><i class="fas fa-home me-2"></i>Imóveis</p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-info mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.totalCorretores}</h2>
                            <p class="card-text"><i class="fas fa-user-tie me-2"></i>Corretores</p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-warning mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.totalVisitas}</h2>
                            <p class="card-text"><i class="fas fa-calendar me-2"></i>Visitas</p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-danger mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.totalContratos}</h2>
                            <p class="card-text"><i class="fas fa-file-contract me-2"></i>Contratos</p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-2 col-md-4 col-6 mb-4">
                    <div class="card text-white bg-purple mb-3">
                        <div class="card-body text-center">
                            <h2 class="card-title mb-0">${stats.visitasHoje}</h2>
                            <p class="card-text"><i class="fas fa-eye me-2"></i>Visitas Hoje</p>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <!-- Status dos Imóveis -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="card">
                        <div class="card-header bg-success text-white">
                            <h6 class="mb-0"><i class="fas fa-chart-pie me-2"></i>Status dos Imóveis</h6>
                        </div>
                        <div class="card-body">
                            <div class="d-flex justify-content-between mb-2">
                                <span>Disponíveis:</span>
                                <strong class="text-success">${stats.imoveisDisponiveis}</strong>
                            </div>
                            <div class="d-flex justify-content-between mb-2">
                                <span>Vendidos:</span>
                                <strong class="text-danger">${stats.imoveisVendidos}</strong>
                            </div>
                            <div class="d-flex justify-content-between">
                                <span>Alugados:</span>
                                <strong class="text-warning">${stats.imoveisAlugados}</strong>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Valor Total em Contratos -->
                <div class="col-lg-4 col-md-6 mb-4">
                    <div class="card">
                        <div class="card-header bg-primary text-white">
                            <h6 class="mb-0"><i class="fas fa-money-bill-wave me-2"></i>Valor em Contratos</h6>
                        </div>
                        <div class="card-body text-center">
                            <h3 class="text-primary mb-0">${formatCurrency(stats.valorTotalContratos)}</h3>
                            <small class="text-muted">Total em contratos ativos</small>
                        </div>
                    </div>
                </div>

                <!-- Ações Rápidas -->
                <div class="col-lg-4 col-md-12 mb-4">
                    <div class="card">
                        <div class="card-header bg-dark text-white">
                            <h6 class="mb-0"><i class="fas fa-bolt me-2"></i>Ações Rápidas</h6>
                        </div>
                        <div class="card-body">
                            <div class="d-grid gap-2">
                                <button class="btn btn-outline-primary btn-sm" onclick="admin.switchView('imoveis')">
                                    <i class="fas fa-plus me-2"></i>Novo Imóvel
                                </button>
                                <button class="btn btn-outline-success btn-sm" onclick="admin.switchView('visitas')">
                                    <i class="fas fa-calendar-plus me-2"></i>Agendar Visita
                                </button>
                                <button class="btn btn-outline-info btn-sm" onclick="admin.switchView('contratos')">
                                    <i class="fas fa-file-contract me-2"></i>Novo Contrato
                                </button>
                                <button class="btn btn-outline-warning btn-refresh">
                                    <i class="fas fa-sync-alt me-2"></i>Atualizar Dados
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="row">
                <div class="col-12">
                    <div class="card">
                        <div class="card-header bg-secondary text-white">
                            <h6 class="mb-0"><i class="fas fa-info-circle me-2"></i>Resumo do Sistema</h6>
                        </div>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-md-6">
                                    <h6>Status do Sistema:</h6>
                                    <span class="badge bg-success"><i class="fas fa-check-circle me-1"></i>Online</span>
                                    <p class="mt-2 mb-0 small text-muted">Sistema integrado com banco de dados em tempo real</p>
                                </div>
                                <div class="col-md-6">
                                    <h6>Última Atualização:</h6>
                                    <span class="text-muted">${new Date().toLocaleString('pt-BR')}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        this.updateContent(content);
    }

    renderUsuarios(usuarios) {
        const rows = usuarios.map(usuario => `
            <tr>
                <td>${usuario.id_usuario}</td>
                <td>${usuario.nome}</td>
                <td>${usuario.email}</td>
                <td>${usuario.telefone}</td>
                <td>${usuario.fk_Perfil_id}</td>
                <td>
                    <button class="btn btn-sm btn-warning btn-edit" data-type="usuario" data-id="${usuario.id_usuario}">Editar</button>
                    <button class="btn btn-sm btn-danger btn-delete" data-type="usuario" data-id="${usuario.id_usuario}">Excluir</button>
                </td>
            </tr>
        `).join('');

        const content = `
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5>Gestão de Usuários</h5>
                    <button class="btn btn-success" onclick="admin.showUsuarioForm()">Novo Usuário</button>
                </div>
                <div class="card-body">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Nome</th>
                                <th>Email</th>
                                <th>Telefone</th>
                                <th>Perfil</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${rows}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
        this.updateContent(content);
    }

    renderImoveis(imoveis) {
        const rows = imoveis.map(imovel => `
            <tr>
                <td>${imovel.id_imovel}</td>
                <td>${imovel.titulo}</td>
                <td>R$ ${imovel.valor}</td>
                <td>${imovel.area}m²</td>
                <td>${imovel.quartos}</td>
                <td>${imovel.status}</td>
                <td>
                    <button class="btn btn-sm btn-warning btn-edit" data-type="imovel" data-id="${imovel.id_imovel}">Editar</button>
                    <button class="btn btn-sm btn-danger btn-delete" data-type="imovel" data-id="${imovel.id_imovel}">Excluir</button>
                </td>
            </tr>
        `).join('');

        const content = `
            <div class="card">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <h5>Gestão de Imóveis</h5>
                    <button class="btn btn-success" onclick="admin.showImovelForm()">Novo Imóvel</button>
                </div>
                <div class="card-body">
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Título</th>
                                <th>Valor</th>
                                <th>Área</th>
                                <th>Quartos</th>
                                <th>Status</th>
                                <th>Ações</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${rows}
                        </tbody>
                    </table>
                </div>
            </div>
        `;
        this.updateContent(content);
    }

    updateContent(html) {
        document.getElementById('admin-content').innerHTML = html;
    }

    showError(message) {
        this.updateContent(`
            <div class="alert alert-danger" role="alert">
                ${message}
            </div>
        `);
    }

    showSuccess(message) {
        this.updateContent(`
            <div class="alert alert-success" role="alert">
                ${message}
            </div>
        `);
    }

    async refreshData() {
        await this.switchView(this.currentView);
        this.showSuccess('Dados atualizados com sucesso!');
    }

    async editItem(type, id) {
        alert(`Editando ${type} com ID ${id}`);
        // Implementar lógica de edição
    }

    async deleteItem(type, id) {
        if (confirm(`Tem certeza que deseja excluir este ${type}?`)) {
            try {
                await this.api[`delete${type.charAt(0).toUpperCase() + type.slice(1)}`](id);
                this.showSuccess(`${type.charAt(0).toUpperCase() + type.slice(1)} excluído com sucesso!`);
                await this.refreshData();
            } catch (error) {
                this.showError('Erro ao excluir item');
            }
        }
    }
}

// Inicializar dashboard quando a página carregar
document.addEventListener('DOMContentLoaded', () => {
    window.admin = new AdminDashboard();
});