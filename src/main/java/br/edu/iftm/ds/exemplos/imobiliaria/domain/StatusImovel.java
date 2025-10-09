package br.edu.iftm.ds.exemplos.imobiliaria.domain;
import jakarta.persistence.*;
@Entity
@Table (name = "Status_Imovel")
public class StatusImovel {
        @Id
        private Integer id_status;
        private String descricao_status;
    }
