// Admin Dashboard for Imobiliaria 3 Irmãos
class AdminDashboard {
    constructor() {
        this.api = window.ImobiliariaAPI;
        this.currentView = 'dashboard';
        this.init();
    }

    init() {
        this.bindEvents();
        this.loadDashboard();
    }

    bindEvents() {
        // Navegação
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const view = e.target.getAttribute('data-view');
                this.switchView(view);
            });
        });

        // Botões de ação
        document.addEventListener('click', (e) => {
            if (e.target.classList.contains('btn-edit')) {
                this.editItem(e.target.dataset.type, e.target.dataset.id);
            } else if (e.target.classList.contains('btn-delete')) {
                this.deleteItem(e.target.dataset.type, e.target.dataset.id);
            } else if (e.target.classList.contains('btn-refresh')) {
                this.refreshData();
            }
        });
    }

    async switchView(view) {
        this.currentView = view;
        
        // Atualizar navegação ativa
        document.querySelectorAll('.nav-link').forEach(link => {
            link.classList.remove('active');
        });
        document.querySelector(`[data-view="${view}"]`).classList.add('active');

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
    }

    async loadDashboard() {
        try {
            const [usuarios, imoveis, visitas, contratos] = await Promise.all([
                this.api.getUsuarios(),
                this.api.getImoveis(),
                this.api.getVisitas(),
                this.api.getContratosAluguel()
            ]);

            const stats = {
                totalUsuarios: usuarios.length,
                totalImoveis: imoveis.length,
                totalVisitas: visitas.length,
                totalContratos: contratos.length
            };

            this.renderDashboard(stats);
        } catch (error) {
            this.showError('Erro ao carregar dashboard');
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
        const content = `
            <div class="row">
                <div class="col-md-3">
                    <div class="card text-white bg-primary mb-3">
                        <div class="card-body">
                            <h5 class="card-title">${stats.totalUsuarios}</h5>
                            <p class="card-text">Usuários</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-white bg-success mb-3">
                        <div class="card-body">
                            <h5 class="card-title">${stats.totalImoveis}</h5>
                            <p class="card-text">Imóveis</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-white bg-warning mb-3">
                        <div class="card-body">
                            <h5 class="card-title">${stats.totalVisitas}</h5>
                            <p class="card-text">Visitas</p>
                        </div>
                    </div>
                </div>
                <div class="col-md-3">
                    <div class="card text-white bg-info mb-3">
                        <div class="card-body">
                            <h5 class="card-title">${stats.totalContratos}</h5>
                            <p class="card-text">Contratos</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-12">
                    <div class="card">
                        <div class="card-header">
                            <h5>Resumo do Sistema</h5>
                        </div>
                        <div class="card-body">
                            <p>Sistema de gestão imobiliária integrado com banco de dados em tempo real.</p>
                            <button class="btn btn-primary btn-refresh">Atualizar Dados</button>
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