package br.edu.iftm.ds.exemplos.imobiliaria.domain;
import jakarta.persistence.*;
public class Corretor {
    @Entity
    @Table(name = "Corretor")
    public class  Coreetor {
        @Id
        private Integer id_corretor;
        private String creci;

        @OneToOne
        @JoinColumn(name ="fk_usuario_id")
        private Usuario usuario;
    }
}
