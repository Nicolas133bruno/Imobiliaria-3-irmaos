package br.edu.iftm.ds.exemplos.imobiliaria.domain;
import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalTime;

@Entity
@Table(name = "Visita")
public class Visita {
    @Id
    private Integer id_visita;
    private LocalDate data_visita;
    private LocalTime hora_visita;
    private String status_visita;

    @ManyToOne
    @JoinColumn(name = "fk_id_usuario")
    private Usuario usuario;

    @ManyToOne
    @JoinColumn(name = "fk_id_corretor")
    private Corretor corretor;

    @ManyToOne
    @JoinColumn(name = "fk_id_imovel")
    private Imovel imovel;
}