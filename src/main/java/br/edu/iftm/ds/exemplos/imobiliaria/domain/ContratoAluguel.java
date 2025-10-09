package br.edu.iftm.ds.exemplos.imobiliaria.domain;
import jakarta.persistence.*;
import java.math.BigDecimal;
import java.time.LocalDate;

@Entity
@Table(name = "Contrato_Aluguel")
public class ContratoAluguel {
    @Id
    private Integer id_contrato_alug;
    private String tipo;
    private LocalDate data_inicio;
    private LocalDate data_fim;
    private BigDecimal valor_mensalidade;

    @ManyToOne
    @JoinColumn(name = "fk_id_usuario")
    private Usuario usuario;

    @ManyToOne
    @JoinColumn(name = "fk_id_imovel")
    private Imovel imovel;
}