package br.edu.iftm.ds.exemplos.imobiliaria.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "Usuario")
public class Usuario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    private String loginUsu;
    private String senhaUsu;

    @ManyToOne
    @JoinColumn(name = "id_Perf")
    private Perfil perfil;

    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }

    public String getLoginUsu() { return loginUsu; }
    public void setLoginUsu(String loginUsu) { this.loginUsu = loginUsu; }

    public String getSenhaUsu() { return senhaUsu; }
    public void setSenhaUsu(String senhaUsu) { this.senhaUsu = senhaUsu; }

    public Perfil getPerfil() { return perfil; }
    public void setPerfil(Perfil perfil) { this.perfil = perfil; }
}
