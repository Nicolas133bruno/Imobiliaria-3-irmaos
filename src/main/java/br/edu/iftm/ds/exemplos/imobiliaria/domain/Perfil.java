
package br.edu.iftm.ds.exemplos.imobiliaria.domain;

import jakarta.persistence.*;

@Entity
@Table(name = "Perfil")
public class Perfil {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id_Perf;
    private String tipo_perf;

    public Integer getId_Perf() { return id_Perf; }
    public void setId_Perf(Integer id_Perf) { this.id_Perf = id_Perf; }

    public String getTipo_perf() { return tipo_perf; }
    public void setTipo_perf(String tipo_perf) { this.tipo_perf = tipo_perf; }
}
