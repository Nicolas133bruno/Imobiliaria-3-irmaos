package br.edu.iftm.ds.exemplos.imobiliaria.domain;
import jakarta.persistence.*;

@Entity
@Table(name = "Endereco")
public class Endereco {
    @Id
    private Integer id_endereco;
    private String logradouro;
    private String numero;
    private String bairro;
    private String complemento;
    private String cidade;
    private String estado;
    private String cep;
}